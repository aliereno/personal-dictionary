from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user

from app.service.dashboard_service import DashboardService

main = Blueprint('main', __name__)
service = DashboardService()


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
def dashboard():
    metric = service.get_dashboard_metric(current_user.id)
    return render_template('pages/index.html', metric=metric)
