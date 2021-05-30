from app.database.models.definition import Definition
from app.repository.dictionary_repository import DictionaryRepository
from app.service.base_service import BaseService


class DefinitionService(BaseService):
    def __init__(self):
        super().__init__(Definition)
        self.repository = DictionaryRepository(Definition)

    def get_definition_by_id(self, definition_id):
        return self.repository.get_by_id(definition_id)
