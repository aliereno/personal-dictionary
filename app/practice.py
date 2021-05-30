from flask import Blueprint, render_template, redirect, url_for, request, jsonify
from flask_login import login_required, current_user

from app.service.practice_service import PracticeService

practice = Blueprint('practice', __name__)
service = PracticeService()


@practice.before_request
@login_required
def before_request():
    """ Protect all of the admin endpoints. """
    if current_user.is_authenticated:
        pass
    else:
        return redirect(url_for('auth.login'))


@practice.route('/practice')
def index():
    return render_template('pages/practice/index.html')


@practice.route('/practice/new', methods=['POST'])
def practice_new_post():
    response = service.practice_new_post(current_user.id)
    if not response:
        return jsonify(message="Minimum 10 words needed to start practice."), 400
    return jsonify(response), 200


@practice.route('/practice/check', methods=['POST'])
def practice_check():
    _json = request.json
    selected_word_id = _json['selected_word_id']
    words_id_list = _json['words_id_list']
    definition_id = _json['definition_id']
    try:
        response = service.practice_check(current_user.id, selected_word_id, definition_id, words_id_list)
        return jsonify(response)
    except Exception as e:
        print(e)
        return jsonify(message='Something went wrong!'), 400
