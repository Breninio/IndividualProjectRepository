# app/__init__.pyc


# local imports
from config import app_config

# third-party imports
from flask import Flask, session
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_cors import CORS, cross_origin
from flask_marshmallow import Marshmallow
import logging
from werkzeug.security import generate_password_hash, check_password_hash
import sys
from flask_jwt import JWT
from flask_jwt_extended import (JWTManager, create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)
from werkzeug.security import safe_str_cmp
from flask_jwt import current_identity
import base64


def configure_logging():
    # register root logging
    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger('werkzeug').setLevel(logging.INFO)




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
    configure_logging()
    Session(app)
    jwt = JWTManager(app)


    # temporary route
    @app.route('/')
    def hello_world():
        session['tmp'] = 'Johnny'
        user = session['tmp']
        print(user)
        return user
        # return 'Hello, World!'

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
