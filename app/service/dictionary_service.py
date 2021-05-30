import datetime
import math

from sqlalchemy import func

from app.database.models.dictionary import Dictionary
from app.repository.dictionary_repository import DictionaryRepository
from app.service.base_service import BaseService
from app.service.search_service import SearchService


class DictionaryService(BaseService):
    def __init__(self):
        super().__init__(Dictionary)
        self.repository = DictionaryRepository(Dictionary)
        self.search_service = SearchService()

    def dictionary_post(self, user_id, word_id):
        check = self.repository.get_by_specific_column(user_id=user_id, word_id=word_id)
        if check:
            return False

        dictionary = Dictionary(word_id, user_id)
        self.repository.save(dictionary)
        return True

    def get_random_dictionaries(self, limit, user_id):
        dictionaries = self.repository.get_by_specific_column_order_limit(func.random(), limit, user_id=user_id)
        return dictionaries

    def calculate_power(self, dictionary, user_id, is_success=True):
        total_value = 0

        normalized_practice_point = dictionary.practice_point
        total_value += normalized_practice_point * 5

        word_search_count = self.search_service.get_count_by_specific_columns(word_id=dictionary.word_id,
                                                                              user_id=user_id)
        total_value += self._calculate_search_power(word_search_count)
        total_value += self._calculate_appeared_power(dictionary.appeared_word_count)
        if is_success:
            total_value += self._calculate_date_power(dictionary.last_date_of_success_solve)
            total_value += self._calculate_initial_bonus_power(dictionary.appeared_word_count)

        return int(total_value)

    def _calculate_date_power(self, last_date_of_success_solve):
        if last_date_of_success_solve:
            now = datetime.datetime.now()
            delta = last_date_of_success_solve - now
            return abs(delta.days) * 5
        return 0

    def _calculate_search_power(self, word_search_count):
        return math.ceil((1 / word_search_count) * 10)

    def _calculate_appeared_power(self, appeared_word_power):
        return math.ceil((1 / appeared_word_power) * 10)

    def _calculate_initial_bonus_power(self, appeared_word_count):
        if appeared_word_count == 1:
            return 50
        return 0
