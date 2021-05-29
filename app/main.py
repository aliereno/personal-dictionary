from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user

main = Blueprint('main', __name__)


@main.before_request
@login_required
def before_request():
    """ Protect all of the admin endpoints. """
    if current_user.is_authenticated:
        pass
    else:
        return redirect(url_for('auth.login'))


@main.route('/')
def index():
    return redirect(url_for('main.dashboard'))


@main.route('/dashboard')
@login_required
def dashboard():
    return render_template('pages/index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('pages/profile.html')
