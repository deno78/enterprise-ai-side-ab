from . import db
from datetime import datetime, timezone


class Payment(db.Model):
    __tablename__ = 'payments'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    reservation_id = db.Column(db.Integer, db.ForeignKey('reservations.id'), unique=True, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    method = db.Column(db.String(50), nullable=False, default='dummy_qr')
    qr_code_data = db.Column(db.Text)
    status = db.Column(db.String(20), nullable=False, default='unpaid')
    paid_at = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    def to_dict(self):
        return {
            'id': self.id,
            'reservation_id': self.reservation_id,
            'amount': self.amount,
            'method': self.method,
            'status': self.status,
            'paid_at': self.paid_at.isoformat() if self.paid_at else None,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }
