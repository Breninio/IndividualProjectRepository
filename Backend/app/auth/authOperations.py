from flask import flash, redirect, render_template, url_for, request, jsonify
from flask_login import login_required, login_user, logout_user, current_user

from . import auth
from .. import db
from ..models import User


@auth.route('/register', methods=['GET', 'POST'])
def register():
    """
    Handle requests to the /register route
    Add an employee to the database through the registration form
    """
    user = User(email=request.json['email'], password=request.json['password'], first_name=request.json['first_name'],
                last_name=request.json['last_name'], role=request.json['role'])

    # add employee to the database
    db.session.add(user)
    db.session.commit()
    flash('You have successfully registered! You may now login.')

    # redirect to the login page
    #return redirect(url_for('auth.login'))

    message = "user added"
    return jsonify(message, 200)


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
    user = User.query.filter_by(email=email).first()
    if user is not None and user.verify_password(
            password):
        # log employee in
        #print(user)
        login_user(user, remember=True)

        message = "user logged in"
        return jsonify(message, 200)

        # redirect to the dashboard page after login
        #return redirect(url_for('home.dashboard'))

        #when login details are incorrect
        #else:
            #flash('Invalid email or password.')

    # load login template
    #return render_template('auth/login.html', form=form, title='Login')


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


