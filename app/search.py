import json

from flask import Blueprint, render_template, redirect, url_for, request, jsonify, current_app
from flask_login import login_required, current_user

from app.service.search_service import SearchService

search = Blueprint('search', __name__)
service = SearchService()


@search.before_request
@login_required
def before_request():
    """ Protect all of the admin endpoints. """
    if current_user.is_authenticated:
        pass
    else:
        return redirect(url_for('auth.login'))


@search.route('/search')
def index():
    return render_template('pages/search/index.html')


@search.route('/search', methods=['POST'])
def index_post():
    # first lookup Word table
    # if it is not exist -> make api call
    _json = request.json
    search = _json['search']
    current_app.logger.info('Username#'+current_user.username + " searched :"+ search)

    response = service.search_post(current_user.id, search)
    current_app.logger.info('Username#'+current_user.username + " search result: "+ response[0].__str__())
    return jsonify(response[0]), response[1]
