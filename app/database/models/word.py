from app.database import db
from app.database.models.base import BaseModel


class Word(BaseModel):
    content = db.Column(db.String(255), unique=True, nullable=False)

    def __init__(self, content):
        self.content = content

    def __str__(self):
        return str(self.id)+" "+ self.content

    def __json__(self):
        return ['id', 'content', 'definitions']

    def get_fields_for_practice(self):
        return {"id": self.id, "content": self.content}
