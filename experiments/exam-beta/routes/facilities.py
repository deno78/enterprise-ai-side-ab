from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from models import db, Facility
from datetime import datetime, date, time

facilities_bp = Blueprint('facilities', __name__, url_prefix='/api/facilities')


@facilities_bp.route('', methods=['GET'])
def list_facilities():
    lang = request.args.get('lang', 'ja')
    query = Facility.query.filter_by(is_active=True)

    q = request.args.get('q', '').strip()
    if q:
        query = query.filter(
            db.or_(
                Facility.name.contains(q),
                Facility.name_en.contains(q),
                Facility.name_zh.contains(q),
                Facility.address.contains(q)
            )
        )

    type_filter = request.args.get('type')
    if type_filter:
        query = query.filter_by(type=type_filter)

    min_price = request.args.get('min_price', type=float)
    if min_price is not None:
        query = query.filter(Facility.price_per_hour >= min_price)

    max_price = request.args.get('max_price', type=float)
    if max_price is not None:
        query = query.filter(Facility.price_per_hour <= max_price)

    capacity = request.args.get('capacity', type=int)
    if capacity:
        query = query.filter(Facility.capacity >= capacity)

    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 20, type=int)
    pagination = query.order_by(Facility.name).paginate(page=page, per_page=per_page, error_out=False)

    return jsonify({
        'items': [f.to_dict(lang) for f in pagination.items],
        'total': pagination.total,
        'page': page,
        'per_page': per_page
    }), 200


@facilities_bp.route('/<int:facility_id>', methods=['GET'])
def get_facility(facility_id):
    lang = request.args.get('lang', 'ja')
    facility = Facility.query.get_or_404(facility_id)
    return jsonify(facility.to_dict(lang)), 200


@facilities_bp.route('/<int:facility_id>/availability', methods=['GET'])
def get_availability(facility_id):
    facility = Facility.query.get_or_404(facility_id)
    date_str = request.args.get('date')
    if not date_str:
        return jsonify({'type': 'error', 'title': 'Bad Request', 'status': 400, 'detail': 'date パラメータが必要です (YYYY-MM-DD)'}), 400

    try:
        target_date = datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        return jsonify({'type': 'error', 'title': 'Bad Request', 'status': 400, 'detail': '日付形式が正しくありません (YYYY-MM-DD)'}), 400

    from models import Reservation
    reservations = Reservation.query.filter(
        Reservation.facility_id == facility_id,
        Reservation.reserved_date == target_date,
        Reservation.status != 'cancelled'
    ).all()

    business_hours = {'open': '09:00', 'close': '21:00'}
    slots = []
    current_h = 9
    while current_h < 21:
        time_slot = f'{current_h:02d}:00'
        is_available = True
        for r in reservations:
            r_start = r.start_time.hour
            r_end = r.end_time.hour
            if r_start <= current_h < r_end:
                is_available = False
                break
        slots.append({'time': time_slot, 'available': is_available})
        current_h += 1

    return jsonify({
        'facility_id': facility_id,
        'date': date_str,
        'slots': slots,
        'business_hours': business_hours
    }), 200


@facilities_bp.route('', methods=['POST'])
@login_required
def create_facility():
    if current_user.role != 'staff':
        return jsonify({'type': 'error', 'title': 'Forbidden', 'status': 403, 'detail': '職員権限が必要です'}), 403

    data = request.get_json()
    if not data:
        return jsonify({'type': 'error', 'title': 'Bad Request', 'status': 400, 'detail': 'リクエストボディが必要です'}), 400

    facility = Facility(
        name=data['name'],
        type=data['type'],
        address=data.get('address', ''),
        capacity=data.get('capacity', 0),
        price_per_hour=data.get('price_per_hour', 0),
        description=data.get('description', '')
    )
    db.session.add(facility)
    db.session.commit()
    return jsonify(facility.to_dict()), 201


@facilities_bp.route('/<int:facility_id>', methods=['PUT'])
@login_required
def update_facility(facility_id):
    if current_user.role != 'staff':
        return jsonify({'type': 'error', 'title': 'Forbidden', 'status': 403, 'detail': '職員権限が必要です'}), 403

    facility = Facility.query.get_or_404(facility_id)
    data = request.get_json()
    if not data:
        return jsonify({'type': 'error', 'title': 'Bad Request', 'status': 400, 'detail': 'リクエストボディが必要です'}), 400

    for field in ['name', 'name_en', 'name_zh', 'type', 'address', 'address_en', 'address_zh',
                  'capacity', 'price_per_hour', 'description', 'description_en', 'description_zh',
                  'image_url', 'is_active']:
        if field in data:
            setattr(facility, field, data[field])

    db.session.commit()
    return jsonify(facility.to_dict()), 200


@facilities_bp.route('/<int:facility_id>', methods=['DELETE'])
@login_required
def delete_facility(facility_id):
    if current_user.role != 'staff':
        return jsonify({'type': 'error', 'title': 'Forbidden', 'status': 403, 'detail': '職員権限が必要です'}), 403

    facility = Facility.query.get_or_404(facility_id)
    facility.is_active = False
    db.session.commit()
    return jsonify({'message': '施設を削除しました'}), 200
