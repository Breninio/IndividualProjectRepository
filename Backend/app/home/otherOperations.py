from flask import flash, redirect, render_template, url_for, request, jsonify, session, make_response
from flask_login import login_required, login_user, logout_user, current_user
import json

from . import home
from .. import db
from ..models import User, LearningActivity, LearningActivitySchema, userActivities


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
    username = request.args.get('username')
    x = LearningActivity.query.filter(LearningActivity.participants.any(email=username)).all()

    # transforming into JSON-serializable objects
    schema = LearningActivitySchema(many=True)
    #projects = schema.dump(project_details)
    projects = schema.dump(x)

    # serializing as JSON
    print(projects)
    return jsonify(projects)


# Get activity endpoint
@home.route('/projectlist/<activityid>', methods=['GET', ])
def get_activity(activityid):
    selected_activity = LearningActivity.query.filter_by(activity_id=activityid).all()

    print(selected_activity)

    # transforming into JSON-serializable objects
    schema = LearningActivitySchema(many=True)
    # projects = schema.dump(project_details)
    activity = schema.dump(selected_activity)

    # serializing as JSON
    print(activity)
    return jsonify(activity), 200


@home.route('/updateHours', methods=['POST',])
def updateHours():
    try:
        client_request = request.get_json()
        user_id = client_request['user_id']
        print(user_id)
        activity_id = client_request['activity_id']
        print(activity_id)
        hours = client_request['hours']
        print(hours['activityHours'])

        #line_item = session.query(userActivities).filter_by(user_id=user_id, activity_id=activity_id).first()
        line_item = session.query(userActivities).join(User).join(LearningActivity).filter(User.user_id == user_id)
        print(line_item)

        db.session.commit()
        flash('You have successfully registered! You may now login.')
        # generate the auth token
        # message = "Registration has been successful"
        # return make_response(jsonify(message)), 201
    except Exception as e:
        responseObject = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
            }
        print(str(e))
        return make_response(jsonify(responseObject)), 401
    else:
        responseObject = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return make_response(jsonify(responseObject)), 202
