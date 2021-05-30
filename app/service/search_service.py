from app.database.models.search import Search
from app.repository.search_repository import SearchRepository
from app.service.base_service import BaseService
from app.service.word_service import WordService


class SearchService(BaseService):
    def __init__(self):
        super().__init__(Search)
        self.repository = SearchRepository(Search)
        self.word_service = WordService()

    def search_post(self, user_id, search):
        response = self.word_service.search_word(search)
        if not response[0]:
            return response[1], response[2]

        self._insert(word_id=response[1].id, user_id=user_id)
        return response[1], response[2]

    def _insert(self, user_id, word_id):
        search = Search(user_id, word_id)
        self.repository.save(search)
