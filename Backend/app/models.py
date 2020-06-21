import bcrypt as bcrypt
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from marshmallow import Schema, fields
import jwt
import datetime
#import app

from . import db
from . import login_manager


#from app import db, login_manager

userActivities = db.Table('user_activities',
                          db.Column('user_id', db.Integer, db.ForeignKey('usertable.user_id')),
                          db.Column('activity_id', db.Integer, db.ForeignKey('activitytable.activity_id')))


class User(UserMixin, db.Model):

    __tablename__ = 'usertable'

    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.String(30), index=True)
    is_cpdChamp = db.Column(db.Boolean, default=False)
    activities = db.relationship('LearningActivity', secondary=userActivities, backref=db.backref('participants'),
                                 lazy='dynamic')

    def __init__(self, email, password, first_name, last_name, role):
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.role = role
        if role == "cpdchamp":
            self.is_cpdChamp = True
        else:
            self.is_cpdChamp = False



    def encode_auth_token(self, user_id):
        """
        Generates the Auth Token
        :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=5),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(
                payload,
                app.config.get('SECRET_KEY'),
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        """
        Validates the auth token
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, app.config.get('SECRET_KEY'))
            is_blacklisted_token = BlacklistToken.check_blacklist(auth_token)
            if is_blacklisted_token:
                return 'Token blacklisted. Please log in again.'
            else:
                return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.email

    @property
    def password(self):
        """
        Prevent pasword from being accessed
        """
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User: {}>'.format(self.email)


# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(email=user_id).first()



class LearningActivity(db.Model):
    """
    Create table for learning opportunities
    """
    __tablename__ = 'activitytable'

    activity_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60), index=True, unique=True)
    description = db.Column(db.String(200), index=True)
    start_date = db.Column(db.Date, index=True)
    end_date = db.Column(db.Date, index=True)
    reason = db.Column(db.String(200), index=True)
    learning = db.Column(db.String(200), index=True)
    application = db.Column(db.String(200), index=True)
    support = db.Column(db.String(200), index=True)


class LearningActivitySchema(Schema):
    activity_id = fields.Number()
    title = fields.Str()
    description = fields.Str()
    start_date = fields.Date()
    end_dare = fields.Date()
    reason = fields.Str()
    learning = fields.Str()
    application = fields.Str()
    support = fields.Str()


class BlacklistToken(db.Model):
    """
    Token Model for storing JWT tokens
    """
    __tablename__ = 'blacklist_tokens'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    token = db.Column(db.String(500), unique=True, nullable=False)
    blacklisted_on = db.Column(db.DateTime, nullable=False)

    def __init__(self, token):
        self.token = token
        self.blacklisted_on = datetime.datetime.now()

    def __repr__(self):
        return '<id: token: {}'.format(self.token)

    @staticmethod
    def check_blacklist(auth_token):
        # check whether auth token has been blacklisted
        res = BlacklistToken.query.filter_by(token=str(auth_token)).first()
        if res:
            return True
        else:
            return False
