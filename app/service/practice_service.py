import datetime
import random

from flask_login import current_user

from app.database.models.practice import Practice
from app.repository.practice_repository import PracticeRepository
from app.service.base_service import BaseService
from app.service.definition_service import DefinitionService
from app.service.dictionary_service import DictionaryService


class PracticeService(BaseService):
    def __init__(self):
        super().__init__(Practice)
        self.repository = PracticeRepository(Practice)
        self.dictionary_service = DictionaryService()
        self.definition_service = DefinitionService()

    def practice_new_post(self, user_id):
        if len(current_user.dictionaries) < 10:
            return None

        dictionaries = self.dictionary_service.get_random_dictionaries(3, user_id)

        response = {}
        random_dict_index = random.randint(0, 2)
        random_index = random.randint(0, len(dictionaries[random_dict_index].word.definitions) - 1)
        response['definition'] = dictionaries[random_dict_index].word.definitions[random_index]
        response['words'] = [x.word.get_fields_for_practice() for x in dictionaries]
        [self.dictionary_service.update(x.id, appeared_word_count=x.appeared_word_count + 1) for x in dictionaries]
        return response

    def practice_check(self, user_id, selected_word_id, definition_id, words_id_list):
        response = {'status': 'error', 'message': 'The answer is wrong!'}
        definition = self.definition_service.get_definition_by_id(definition_id)
        practice = Practice(user_id, definition_id, selected_word_id)
        selected_dictionary = self.dictionary_service.get_by_specific_column(word_id=selected_word_id, user_id=user_id)
        if str(definition.word_id) == selected_word_id:
            practice.is_success = True
            response = {'status': 'success', 'message': 'Well done!'}

            selected_dictionary.practice_point = selected_dictionary.practice_point + 1
            self.dictionary_service.update(selected_dictionary.id,
                                           last_date_of_success_solve=datetime.datetime.now(),
                                           practice_point=selected_dictionary.practice_point,
                                           power=self.dictionary_service.calculate_power(selected_dictionary,
                                                                                         user_id, True))
        else:
            for item_id in words_id_list:
                point = -1
                if item_id == selected_word_id:
                    point = -2
                dictionary = self.dictionary_service.get_by_specific_column(word_id=item_id,
                                                                            user_id=user_id)
                dictionary.practice_point = dictionary.practice_point + point
                self.dictionary_service.update(dictionary.id,
                                               practice_point=dictionary.practice_point,
                                               power=self.dictionary_service.calculate_power(dictionary, user_id,
                                                                                             False))

        self.repository.save(practice)
        return response
