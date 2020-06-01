# app/__init__.py

# third-party imports
from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_cors import CORS, cross_origin
from flask_marshmallow import Marshmallow


# local imports
from config import app_config

# db variable initialization
db = SQLAlchemy()
# login manager initialization
login_manager = LoginManager()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    CORS(app, resources={r"*": {"origins": "*"}})
    db.init_app(app)
    ma = Marshmallow(app)

    # temporary route
    @app.route('/')
    def hello_world():
        return 'Hello, World!'

    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page."
    login_manager.login_view = "auth.login"

    migrate = Migrate(app, db)

    from app import models

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    return app
