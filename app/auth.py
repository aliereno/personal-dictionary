from flask import Blueprint, render_template, request, jsonify, session, redirect, url_for, current_app
from flask_login import logout_user, current_user

from .service.auth_service import AuthService

auth = Blueprint('auth', __name__)
service = AuthService()


@auth.route('/login')
def login():
    return render_template('pages/auth/login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    _json = request.json
    username = _json['username']
    password = _json['password']
    current_app.logger.info('Username#'+username + " tried to login.")

    if service.login(username, password):
        session['username'] = username
        return jsonify(message="Success, you will be redirected.")
    else:
        return jsonify(loggedIn=False, error='Invalid Email/Password'), 400


@auth.route('/signup')
def signup():
    return render_template('pages/auth/signup.html')


@auth.route('/signup', methods=['POST'])
def signup_post():
    _json = request.json
    username = _json['username']
    password = _json['password']

    if service.signup(username, password):
        return jsonify(message='Success, you can login now.'), 201
    return jsonify(error='Username already exists.'), 400


@auth.route('/logout')
def logout():
    current_app.logger.info('Username#'+current_user.username + " logged out.")
    logout_user()
    return redirect(url_for('auth.login'))
