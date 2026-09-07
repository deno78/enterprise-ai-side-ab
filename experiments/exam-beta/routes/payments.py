from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from models import db, Payment, Reservation
from datetime import datetime, timezone
import qrcode
import io
import base64

payments_bp = Blueprint('payments', __name__, url_prefix='/api/payments')


@payments_bp.route('/<int:reservation_id>/pay', methods=['POST'])
@login_required
def make_payment(reservation_id):
    reservation = Reservation.query.get_or_404(reservation_id)
    if reservation.user_id != current_user.id:
        return jsonify({'type': 'error', 'title': 'Forbidden', 'status': 403, 'detail': 'アクセス権限がありません'}), 403

    if reservation.status == 'cancelled':
        return jsonify({'type': 'error', 'title': 'Bad Request', 'status': 400, 'detail': 'キャンセル済みの予約は決済できません'}), 400

    existing_payment = Payment.query.filter_by(reservation_id=reservation_id).first()
    if existing_payment and existing_payment.status == 'paid':
        return jsonify({'payment_id': existing_payment.id, 'amount': existing_payment.amount, 'status': 'paid'}), 200

    facility = reservation.facility
    hours = (datetime.combine(datetime.min, reservation.end_time) - datetime.combine(datetime.min, reservation.start_time)).total_seconds() / 3600
    amount = int(hours * facility.price_per_hour)

    qr_data = f'PAYMENT:RESERVATION:{reservation_id}:AMOUNT:{amount}'

    qr_img = qrcode.make(qr_data)
    buf = io.BytesIO()
    qr_img.save(buf, format='PNG')
    qr_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
    qr_data_uri = f'data:image/png;base64,{qr_base64}'

    if existing_payment:
        existing_payment.status = 'paid'
        existing_payment.qr_code_data = qr_data_uri
        existing_payment.paid_at = datetime.now(timezone.utc)
        payment = existing_payment
    else:
        payment = Payment(
            reservation_id=reservation_id,
            amount=amount,
            method='dummy_qr',
            qr_code_data=qr_data_uri,
            status='paid',
            paid_at=datetime.now(timezone.utc)
        )
        db.session.add(payment)

    reservation.status = 'confirmed'
    db.session.commit()

    return jsonify({
        'payment_id': payment.id,
        'amount': amount,
        'qr_code_data': qr_data_uri,
        'status': 'paid'
    }), 200


@payments_bp.route('/<int:reservation_id>', methods=['GET'])
@login_required
def get_payment(reservation_id):
    reservation = Reservation.query.get_or_404(reservation_id)
    if reservation.user_id != current_user.id and current_user.role != 'staff':
        return jsonify({'type': 'error', 'title': 'Forbidden', 'status': 403, 'detail': 'アクセス権限がありません'}), 403

    payment = Payment.query.filter_by(reservation_id=reservation_id).first()
    if not payment:
        return jsonify({'type': 'error', 'title': 'Not Found', 'status': 404, 'detail': '決済情報が見つかりません'}), 404

    return jsonify(payment.to_dict()), 200
