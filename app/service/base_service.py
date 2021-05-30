from app.repository.base_repository import BaseRepository


class BaseService:
    def __init__(self, model):
        self.repository = BaseRepository(model)

    def get_by_id(self, id):
        return self.repository.get_by_id(id)

    def get_by_specific_column(self, **kwargs):
        return self.repository.get_by_specific_column(**kwargs)

    def get_all_by_specific_column(self, **kwargs):
        return self.repository.get_all_by_specific_column(**kwargs)

    def get_count_by_specific_columns(self, **kwargs):
        return self.repository.get_count_by_specific_columns(**kwargs)

    def update(self, id, **kwargs):
        self.repository.update(id, **kwargs)
