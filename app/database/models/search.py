from app.database import db
from app.database.models.base import BaseModel


class Search(BaseModel):
    word_id = db.Column(db.Integer, db.ForeignKey('word.id'), nullable=False)
    word = db.relationship('Word', backref=db.backref('searches', lazy=True, cascade="save-update"))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('searches', lazy=True))

    def __init__(self, user_id, word_id=None):
        self.word_id = word_id
        self.user_id = user_id
