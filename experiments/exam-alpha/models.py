from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    lang = db.Column(db.String(10), default='ja')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    reservations = db.relationship('Reservation', backref='user', lazy=True)


class Facility(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_ja = db.Column(db.String(200), nullable=False)
    name_en = db.Column(db.String(200), nullable=False)
    name_zh = db.Column(db.String(200), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    location_ja = db.Column(db.String(200), nullable=False)
    location_en = db.Column(db.String(200), nullable=False)
    location_zh = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    description_ja = db.Column(db.Text)
    description_en = db.Column(db.Text)
    description_zh = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    reservations = db.relationship('Reservation', backref='facility', lazy=True)

    def to_dict(self, lang='ja'):
        return {
            'id': self.id,
            'name': getattr(self, f'name_{lang}'),
            'type': self.type,
            'location': getattr(self, f'location_{lang}'),
            'price': self.price,
            'capacity': self.capacity,
            'description': getattr(self, f'description_{lang}'),
        }


class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    facility_id = db.Column(db.Integer, db.ForeignKey('facility.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    start_time = db.Column(db.String(5), nullable=False)
    end_time = db.Column(db.String(5), nullable=False)
    num_people = db.Column(db.Integer, nullable=False)
    purpose = db.Column(db.String(500))
    purpose_ja = db.Column(db.String(500))
    purpose_en = db.Column(db.String(500))
    purpose_zh = db.Column(db.String(500))
    status = db.Column(db.String(20), default='confirmed')
    payment_status = db.Column(db.String(20), default='unpaid')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self, lang='ja'):
        purpose_key = f'purpose_{lang}' if lang != 'ja' and hasattr(self, f'purpose_{lang}') and getattr(self, f'purpose_{lang}') else 'purpose'
        return {
            'id': self.id,
            'user_id': self.user_id,
            'facility_id': self.facility_id,
            'facility_name': getattr(self.facility, f'name_{lang}'),
            'facility_location': getattr(self.facility, f'location_{lang}'),
            'facility_type': self.facility.type,
            'date': self.date.isoformat() if isinstance(self.date, date) else self.date,
            'start_time': self.start_time,
            'end_time': self.end_time,
            'num_people': self.num_people,
            'purpose': getattr(self, purpose_key) or self.purpose,
            'status': self.status,
            'payment_status': self.payment_status,
            'price': self.facility.price,
            'created_at': self.created_at.isoformat() if isinstance(self.created_at, datetime) else self.created_at,
        }
