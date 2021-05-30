from app.repository.base_repository import BaseRepository


class SearchRepository(BaseRepository):
    def __init__(self, model):
        super().__init__(model)
