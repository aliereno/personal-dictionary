from app.repository.base_repository import BaseRepository


class PracticeRepository(BaseRepository):
    def __init__(self, model):
        super().__init__(model)
