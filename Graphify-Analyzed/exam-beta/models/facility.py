from . import db
from datetime import datetime, timezone


class Facility(db.Model):
    __tablename__ = 'facilities'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200), nullable=False)
    name_en = db.Column(db.String(200))
    name_zh = db.Column(db.String(200))
    type = db.Column(db.String(50), nullable=False, index=True)
    address = db.Column(db.String(300), nullable=False)
    address_en = db.Column(db.String(300))
    address_zh = db.Column(db.String(300))
    capacity = db.Column(db.Integer, nullable=False)
    price_per_hour = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text)
    description_en = db.Column(db.Text)
    description_zh = db.Column(db.Text)
    image_url = db.Column(db.String(500))
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    reservations = db.relationship('Reservation', backref='facility', lazy='dynamic')

    def to_dict(self, lang='ja'):
        name_key = f'name_{lang}' if lang != 'ja' else 'name'
        addr_key = f'address_{lang}' if lang != 'ja' else 'address'
        desc_key = f'description_{lang}' if lang != 'ja' else 'description'

        return {
            'id': self.id,
            'name': getattr(self, name_key) or self.name,
            'type': self.type,
            'address': getattr(self, addr_key) or self.address,
            'capacity': self.capacity,
            'price_per_hour': self.price_per_hour,
            'description': getattr(self, desc_key) or self.description,
            'image_url': self.image_url,
            'is_active': self.is_active
        }
