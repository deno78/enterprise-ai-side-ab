from flask import Blueprint, request, jsonify, send_file
from flask_login import login_required, current_user
from models import db, Reservation, Facility, ReservationLog
from services.pdf_service import generate_reservation_pdf
from datetime import datetime, date, time
import io

reservations_bp = Blueprint('reservations', __name__, url_prefix='/api/reservations')


@reservations_bp.route('', methods=['GET'])
@login_required
def list_reservations():
    query = Reservation.query

    if current_user.role != 'staff':
        query = query.filter_by(user_id=current_user.id)
    else:
        user_id = request.args.get('user_id', type=int)
        if user_id:
            query = query.filter_by(user_id=user_id)

    status_filter = request.args.get('status')
    if status_filter:
        query = query.filter_by(status=status_filter)

    reservations = query.order_by(Reservation.reserved_date.desc()).all()
    return jsonify({'items': [r.to_dict() for r in reservations], 'total': len(reservations)}), 200


@reservations_bp.route('', methods=['POST'])
@login_required
def create_reservation():
    data = request.get_json()
    if not data:
        return jsonify({'type': 'error', 'title': 'Bad Request', 'status': 400, 'detail': 'リクエストボディが必要です'}), 400

    facility_id = data.get('facility_id')
    reserved_date_str = data.get('reserved_date')
    start_time_str = data.get('start_time')
    end_time_str = data.get('end_time')
    number_of_people = data.get('number_of_people', 1)
    purpose = data.get('purpose', '')

    errors = {}
    if not facility_id:
        errors['facility_id'] = '施設IDは必須です'

    facility = Facility.query.get(facility_id)
    if not facility:
        errors['facility_id'] = '指定された施設が見つかりません'

    try:
        reserved_date = datetime.strptime(reserved_date_str, '%Y-%m-%d').date()
    except (ValueError, TypeError):
        errors['reserved_date'] = '日付形式が正しくありません (YYYY-MM-DD)'

    try:
        start_time = datetime.strptime(start_time_str, '%H:%M').time()
    except (ValueError, TypeError):
        errors['start_time'] = '時刻形式が正しくありません (HH:MM)'

    try:
        end_time = datetime.strptime(end_time_str, '%H:%M').time()
    except (ValueError, TypeError):
        errors['end_time'] = '時刻形式が正しくありません (HH:MM)'

    if errors:
        return jsonify({
            'type': 'https://example.com/errors/validation-error',
            'title': 'Validation Error',
            'status': 400,
            'detail': '入力内容に誤りがあります',
            'instance': '/api/reservations',
            'errors': errors
        }), 400

    if number_of_people > facility.capacity:
        return jsonify({
            'type': 'https://example.com/errors/validation-error',
            'title': 'Capacity Exceeded',
            'status': 400,
            'detail': f'収容人数({facility.capacity}人)を超えています',
            'instance': '/api/reservations',
            'errors': {'number_of_people': f'最大{facility.capacity}人までです'}
        }), 400

    conflict = Reservation.query.filter(
        Reservation.facility_id == facility_id,
        Reservation.reserved_date == reserved_date,
        Reservation.status != 'cancelled',
        Reservation.start_time < end_time,
        Reservation.end_time > start_time
    ).first()

    if conflict:
        return jsonify({
            'type': 'https://example.com/errors/conflict',
            'title': 'Conflict',
            'status': 409,
            'detail': '指定された時間帯は既に予約されています',
            'instance': '/api/reservations'
        }), 409

    hours = (datetime.combine(date.min, end_time) - datetime.combine(date.min, start_time)).total_seconds() / 3600
    amount = int(hours * facility.price_per_hour)

    reservation = Reservation(
        user_id=current_user.id,
        facility_id=facility_id,
        reserved_date=reserved_date,
        start_time=start_time,
        end_time=end_time,
        number_of_people=number_of_people,
        purpose=purpose,
        status='pending'
    )
    db.session.add(reservation)
    db.session.flush()

    log = ReservationLog(
        reservation_id=reservation.id,
        action='created',
        details=f'施設: {facility.name}, 日時: {reserved_date} {start_time_str}-{end_time_str}',
        user_id=current_user.id
    )
    db.session.add(log)
    db.session.commit()

    return jsonify({
        'id': reservation.id,
        'message': '予約を受け付けました',
        'amount': amount,
        'status': 'pending'
    }), 201


@reservations_bp.route('/<int:reservation_id>', methods=['GET'])
@login_required
def get_reservation(reservation_id):
    reservation = Reservation.query.get_or_404(reservation_id)
    if current_user.role != 'staff' and reservation.user_id != current_user.id:
        return jsonify({'type': 'error', 'title': 'Forbidden', 'status': 403, 'detail': 'アクセス権限がありません'}), 403
    return jsonify(reservation.to_dict()), 200


@reservations_bp.route('/<int:reservation_id>', methods=['PUT'])
@login_required
def update_reservation(reservation_id):
    reservation = Reservation.query.get_or_404(reservation_id)
    if reservation.user_id != current_user.id:
        return jsonify({'type': 'error', 'title': 'Forbidden', 'status': 403, 'detail': 'アクセス権限がありません'}), 403
    if reservation.status == 'cancelled':
        return jsonify({'type': 'error', 'title': 'Bad Request', 'status': 400, 'detail': 'キャンセル済みの予約は変更できません'}), 400

    data = request.get_json()
    if not data:
        return jsonify({'type': 'error', 'title': 'Bad Request', 'status': 400, 'detail': 'リクエストボディが必要です'}), 400

    if 'reserved_date' in data:
        reservation.reserved_date = datetime.strptime(data['reserved_date'], '%Y-%m-%d').date()
    if 'start_time' in data:
        reservation.start_time = datetime.strptime(data['start_time'], '%H:%M').time()
    if 'end_time' in data:
        reservation.end_time = datetime.strptime(data['end_time'], '%H:%M').time()
    if 'number_of_people' in data:
        reservation.number_of_people = data['number_of_people']
    if 'purpose' in data:
        reservation.purpose = data['purpose']

    log = ReservationLog(
        reservation_id=reservation.id,
        action='modified',
        user_id=current_user.id
    )
    db.session.add(log)
    db.session.commit()

    return jsonify({'message': '予約を変更しました', 'reservation': reservation.to_dict()}), 200


@reservations_bp.route('/<int:reservation_id>', methods=['DELETE'])
@login_required
def cancel_reservation(reservation_id):
    reservation = Reservation.query.get_or_404(reservation_id)
    if reservation.user_id != current_user.id and current_user.role != 'staff':
        return jsonify({'type': 'error', 'title': 'Forbidden', 'status': 403, 'detail': 'アクセス権限がありません'}), 403

    reservation.status = 'cancelled'
    log = ReservationLog(
        reservation_id=reservation.id,
        action='cancelled',
        user_id=current_user.id
    )
    db.session.add(log)
    db.session.commit()

    return jsonify({'message': '予約をキャンセルしました'}), 200


@reservations_bp.route('/<int:reservation_id>/pdf', methods=['GET'])
@login_required
def download_pdf(reservation_id):
    reservation = Reservation.query.get_or_404(reservation_id)
    if reservation.user_id != current_user.id and current_user.role != 'staff':
        return jsonify({'type': 'error', 'title': 'Forbidden', 'status': 403, 'detail': 'アクセス権限がありません'}), 403

    pdf_buffer = generate_reservation_pdf(reservation)
    return send_file(
        pdf_buffer,
        mimetype='application/pdf',
        as_attachment=True,
        download_name=f'reservation_{reservation.id}.pdf'
    )
