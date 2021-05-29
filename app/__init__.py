from flask import Flask
from flask_login import LoginManager

from app.database import db, migrate
from app.database.models.user import User


def create_app():
    app = Flask(__name__, static_folder="templates/static")

    app.config['SECRET_KEY'] = 'secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    db.init_app(app)
    migrate.init_app(app, db)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(userid):
        try:
            return db.session.query(User).filter(User.id == userid).first()
        except User.DoesNotExist:
            return None

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
