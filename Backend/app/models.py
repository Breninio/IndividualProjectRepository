from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from marshmallow import Schema, fields

from app import db, login_manager

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



    #email = db.Column(db.String(50), primary_key=True)
    #password = db.Column(db.String(255))
    #firstname = db.Column(db.String(50))
    #surname = db.Column(db.String(50))
    #role = db.Column(db.String(50))


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