from app.database import db
from app.database.models.base import BaseModel


class Dictionary(BaseModel):
    word_id = db.Column(db.Integer, db.ForeignKey('word.id'), nullable=False)
    word = db.relationship('Word', backref=db.backref('dictionaries', lazy=True))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('dictionaries', lazy=True))

    power = db.Column(db.Integer, default=0)
    practice_point = db.Column(db.Integer, default=0)
    appeared_word_count = db.Column(db.Integer, default=0)
    last_date_of_success_solve = db.Column(db.DateTime, nullable=True)

    def __init__(self, word_id, user_id):
        self.word_id = word_id
        self.user_id = user_id
