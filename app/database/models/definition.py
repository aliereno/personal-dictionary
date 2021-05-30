from app.database import db
from app.database.models.base import BaseModel


class Definition(BaseModel):
    content = db.Column(db.String(255), unique=True, nullable=False)
    part_of_speech = db.Column(db.String(255), nullable=False)
    word_id = db.Column(db.Integer, db.ForeignKey('word.id'), nullable=False)
    word = db.relationship('Word', backref=db.backref('definitions', lazy=True, cascade="save-update"))

    def __init__(self, content, part_of_speech, word_id=None):
        self.word_id = word_id
        self.content = content
        self.part_of_speech = part_of_speech

    def __json__(self):
        return ['id', 'content', 'part_of_speech']
