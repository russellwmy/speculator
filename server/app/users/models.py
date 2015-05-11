from datetime import datetime
from app import app
from app import db


class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String)
    username = db.Column(db.String)
    password = db.Column(db.String)

    status = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

    def verify_password(self, password):
        import hashlib
        salt = app.config.get('SECRET')
        password = hashlib.sha512( (salt + password).encode('utf-8') ).hexdigest()
        return self.password == password

    def set_password(self, password):
        import hashlib
        salt = app.config.get('SECRET')
        self.password = hashlib.sha512( (salt + password).encode('utf-8') ).hexdigest()

