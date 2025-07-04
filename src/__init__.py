from flask import Flask
from flask_admin.menu import MenuLink

from src.config import Config
from src.ext import db, migrate, login_manager, admin
from src.views import main_blueprint, auth_blueprint, course_blueprint
from src.commands import init_db, populate_db
from src.commands import init_db, populate_db
from src.models.user import User
from src.models.course import Course
from src.admin_views.base import SecureModelView
from src.admin_views.user import UserView
from src.admin_views.course import CourseView

BLUEPRINTS = [main_blueprint, auth_blueprint, course_blueprint]
COMMANDS = [init_db, populate_db]


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    register_extensions(app)
    register_blueprints(app)
    register_commands(app)

    return app


def register_extensions(app):
    # Flask-SQLAlchemy
    db.init_app(app)

    # Flask-Migrate
    migrate.init_app(app, db)

    # Flask-Login
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(_id):
        return User.query.get(_id)

    # Flask-Admin
    admin.init_app(app)
    admin.add_view(UserView(User, db.session))
    admin.add_view(CourseView(Course, db.session))

    admin.add_link(MenuLink("To Site", url="/", icon_type="fa", icon_value="fa-sign-out"))


def register_blueprints(app):
    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint)


def register_commands(app):
    for command in COMMANDS:
        app.cli.add_command(command)