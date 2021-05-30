from flask_login import login_user
from werkzeug.security import check_password_hash, generate_password_hash

from app import User
from app.repository.auth_repository import AuthRepository
from app.service.base_service import BaseService


class AuthService(BaseService):
    def __init__(self):
        super().__init__(User)
        self.repository = AuthRepository(User)

    def login(self, username, password):
        user = self.repository.get_by_specific_column(username=username)
        if user and check_password_hash(user.password, password):
            logged_in_user = user
            login_user(logged_in_user)
            return True
        else:
            return False

    def signup(self, username, password):
        user = self.repository.get_by_specific_column(username=username)
        if user:
            return False
        new_user = User(username=username, password=generate_password_hash(password, method='sha256'))
        self.repository.save(new_user)
        return True
