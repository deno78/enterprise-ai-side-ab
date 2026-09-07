from . import db
from datetime import datetime, timezone


class Reservation(db.Model):
    __tablename__ = 'reservations'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    facility_id = db.Column(db.Integer, db.ForeignKey('facilities.id'), nullable=False, index=True)
    reserved_date = db.Column(db.Date, nullable=False, index=True)
    start_time = db.Column(db.Time, nullable=False)
    end_time = db.Column(db.Time, nullable=False)
    number_of_people = db.Column(db.Integer, nullable=False)
    purpose = db.Column(db.String(500))
    status = db.Column(db.String(20), nullable=False, default='pending')
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    payment = db.relationship('Payment', backref='reservation', uselist=False)
    logs = db.relationship('ReservationLog', backref='reservation', lazy='dynamic')

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'facility_id': self.facility_id,
            'facility_name': self.facility.name if self.facility else None,
            'reserved_date': self.reserved_date.isoformat() if self.reserved_date else None,
            'start_time': self.start_time.strftime('%H:%M') if self.start_time else None,
            'end_time': self.end_time.strftime('%H:%M') if self.end_time else None,
            'number_of_people': self.number_of_people,
            'purpose': self.purpose,
            'status': self.status,
            'payment_status': self.payment.status if self.payment else None,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }
