from flask import Blueprint, render_template, request, jsonify, session, redirect, url_for
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

from app.database.models.user import User
from . import db

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('pages/auth/login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    # TODO: add rate limiter
    _json = request.json
    username = _json['username']
    password = _json['password']

    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        logged_in_user = user
        login_user(logged_in_user)
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

    # check user existence
    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify(error='Username already exists.'), 400

    new_user = User(username=username, password=generate_password_hash(password, method='sha256'))

    db.session.add(new_user)
    db.session.commit()

    return jsonify(message='Success, you can login now.'), 201


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
