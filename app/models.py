from app import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(35), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    clicks = db.Column(db.Integer, default=0)

    def increment_clicks(self):
        self.clicks += 1
