from flask import flash, redirect, render_template, url_for, request, jsonify, session
from flask_login import login_required, login_user, logout_user, current_user

from . import home
from .. import db
from ..models import User, LearningActivity, LearningActivitySchema


@home.route('/new', methods=['GET', 'POST'])
def addactivity():
    """
    Handle requests to the /register route
    Add an employee to the database through the registration form
    """
    activity = LearningActivity(title=request.json['activity_title'], description=request.json['activity_description'],
                                start_date=request.json['activity_startDate'],
                                end_date=request.json['activity_endDate'], reason=request.json['activity_reason'],
                                learning=request.json['activity_learnings'],
                                application=request.json['activity_application'],
                                support=request.json['activity_support'])

    participant1 = User.query.filter_by(email=request.json['activity_participant1']).first()

    activity.participants.append(participant1)

    # add activity to the database
    db.session.add(activity)
    db.session.commit()
    flash('You have successfully added the activity')


    # redirect to the login page
    #return redirect(url_for('auth.login'))

    message = "activity added"
    return jsonify(message, 200)


@home.route("/projectlist", methods=['GET', 'POST'])
#@login_required
def getprojects():
    #project_details = LearningActivity.query.all()
    #print(current_user.email)
    print(session['username'])
    x = LearningActivity.query.filter(LearningActivity.participants.any(email=session['username'])).all()

    # transforming into JSON-serializable objects
    schema = LearningActivitySchema(many=True)
    #projects = schema.dump(project_details)
    projects = schema.dump(x)

    # serializing as JSON
    #print(projects)
    return jsonify(projects)
