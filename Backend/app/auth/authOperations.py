from flask import flash, redirect, render_template, url_for, request, jsonify, session, logging, make_response
from flask_jwt_extended import create_access_token, create_refresh_token
from flask_login import login_required, login_user, logout_user, current_user
from flask import current_app
from werkzeug.security import generate_password_hash, check_password_hash

from . import auth
from .. import db
from ..models import User

@auth.route('/register', methods=['GET', 'POST'])
def register():
    """
    Handle requests to the /register route
    Add an employee to the database through the registration form
    """
    check_user = User.query.filter_by(email=request.json['email']).first()

    if not check_user:
        print("no user found")
        try:
            client_request = request.get_json()
            email = client_request['email']
            print(email)
            password = client_request['password']
            print(password)
            first_name = client_request['first_name']
            print(first_name)
            last_name = client_request['last_name']
            print(last_name)
            role = client_request['role']
            print(role)
            user = User(email=email, password=password, first_name=first_name, last_name=last_name, role=role)
            # add employee to the database
            #print(user)
            db.session.add(user)
            db.session.commit()
            flash('You have successfully registered! You may now login.')
            # generate the auth token

            message = "Registration has been successful"

            return make_response(jsonify(message)), 201
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

    # redirect to the login page
    #return redirect(url_for('auth.login'))


@auth.route('/login', methods=['GET', 'POST'])
def login():
    """
    Handle requests to the /login route
    Log an employee in through the login form
    """
    email = request.json['email']
    print(email)
    password = request.json['password']
    print(password)


    # check whether employee exists in the database and whether
    # the password entered matches the password in the database
    try:
        user = User.query.filter_by(email=email).first()
        if user is not None and user.verify_password(password):
            print("found user")
            print(user)
            login_user(user, remember=True)
            current_app.logger.info('%s logged in successfully', user.email)
            access_token = create_access_token(identity=request.json['email'])
            refresh_token = create_refresh_token(identity=request.json['email'])
            return jsonify({
                'message': 'login successful',
                'access_token': access_token,
                'refresh_token': refresh_token,
                'username': email,
                'role': user.role,
                'id': user.user_id,
            }), 200

        else:
            responseObject = {
                'status': 'fail',
                'message': 'User does not exist.'
            }
            return make_response(jsonify(responseObject)), 404

    except Exception as e:
        current_app.logger.info('Login Failed')
        print(e)
        responseObject = {
            'status': 'fail',
            'message': 'Try again'
        }
        return make_response(jsonify(responseObject)), 500


@auth.route('/logout')
@login_required
def logout():
    """
    Handle requests to the /logout route
    Log an employee out through the logout link
    """
    logout_user()
    flash('You have successfully been logged out.')

    # redirect to the login page
    return redirect(url_for('auth.login'))


