from flask_login import UserMixin

from app.database import db
from app.database.models.base import BaseModel


class User(BaseModel, UserMixin):
    username = db.Column(db.String(1000), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password
    def __repr__(self):
        return '<User %r>' % self.username
