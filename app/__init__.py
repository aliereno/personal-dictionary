import logging
import os

from flask import Flask
from flask_login import LoginManager

from app.database import db, migrate
from app.database.models.user import User
from app.utils.json_encoder import AlchemyEncoder


def create_app():
    app = Flask(__name__, static_folder="templates/static")

    app.json_encoder = AlchemyEncoder

    app.config['SECRET_KEY'] = 'secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['APP_LOG_NAME'] = os.environ.get("APP_LOG_NAME", "app.log")

    logging.basicConfig(filename=os.environ.get("APP_LOG_NAME", "app.log"), level=logging.DEBUG,
                    format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

    db.init_app(app)
    migrate.init_app(app, db)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(userid):
        try:
            return db.session.query(User).filter(User.id == userid).first()
        except Exception as e:

            return None

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .search import search as search_blueprint
    app.register_blueprint(search_blueprint)

    from .dictionary import dictionary as dictionary_blueprint
    app.register_blueprint(dictionary_blueprint)

    from .practice import practice as practice_blueprint
    app.register_blueprint(practice_blueprint)

    return app
