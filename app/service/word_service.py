import os

import requests

from app.database.models.definition import Definition
from app.database.models.word import Word
from app.repository.word_repository import WordRepository
from app.service.base_service import BaseService


class WordService(BaseService):
    def __init__(self):
        super().__init__(Word)
        self.repository = WordRepository(Word)

    def search_word(self, search):
        word_db = self.repository.get_by_specific_column(content=search)
        if not word_db:
            api_call_url = os.environ.get('WORDS_API_URL') + search + "/definitions"

            headers = {
                'x-rapidapi-key': os.environ.get('X-RAPIDAPI-KEY'),
                'x-rapidapi-host': "wordsapiv1.p.rapidapi.com"
            }

            resp = requests.request("GET", api_call_url, headers=headers)
            data = resp.json()
            if resp.status_code != 200:
                return False, {"message": data['message'], "status": "Error"}, 400

            if 'word' in data:
                word = Word(data['word'])
                if ('definitions' in data) and (len(data['definitions']) > 0):
                    definition_list = []
                    for definition in data['definitions']:
                        new_definition = Definition(content=definition['definition'],
                                                    part_of_speech=definition['partOfSpeech'])
                        definition_list.append(new_definition)

                    word.definitions = definition_list

                self.repository.save(word)
                word_db = word
        return True, word_db, 200
