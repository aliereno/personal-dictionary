from app.service.dictionary_service import DictionaryService
from app.service.practice_service import PracticeService
from app.service.search_service import SearchService
from app.service.word_service import WordService


class DashboardService:
    def __init__(self):
        self.dictionary_service = DictionaryService()
        self.word_service = WordService()
        self.search_service = SearchService()
        self.practice_service = PracticeService()

    def get_dashboard_metric(self, user_id):
        response = {}
        response['total_word'] = self.dictionary_service.get_count_by_specific_columns(user_id=user_id)
        response['search_count'] = self.search_service.get_count_by_specific_columns(user_id=user_id)
        response['total_practice'] = self.practice_service.get_count_by_specific_columns(user_id=user_id)
        response['success_ratio'] = ''
        all_practice = self.practice_service.get_all_by_specific_column(user_id=user_id)
        success_count = 0
        fail_count = 0
        for practice in all_practice:
            if practice.is_success:
                success_count += 1
            else:
                fail_count += 1

        print(success_count, " ", fail_count)
        if (success_count + fail_count) != 0:
            response['success_ratio'] = int((success_count / (success_count + fail_count)) * 100)

        return response
