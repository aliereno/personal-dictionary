from app.database import db
from app.database.models.base import BaseModel


class Practice(BaseModel):
    is_success = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('practices', lazy=True))
    definition_id = db.Column(db.Integer, db.ForeignKey('definition.id'), nullable=False)
    definition = db.relationship('Definition', backref=db.backref('practices', lazy=True))
    selected_word_id = db.Column(db.Integer, db.ForeignKey('word.id'), nullable=False)
    selected_word = db.relationship('Word', backref=db.backref('practices', lazy=True))

    def __init__(self, user_id, definition_id, selected_word_id, is_success=False):
        self.user_id = user_id
        self.definition_id = definition_id
        self.selected_word_id = selected_word_id
        self.is_success = is_success
