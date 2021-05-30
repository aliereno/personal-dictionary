from flask import Blueprint, render_template, redirect, url_for, request, jsonify
from flask_login import login_required, current_user

from app.service.dictionary_service import DictionaryService

dictionary = Blueprint('dictionary', __name__)
service = DictionaryService()


@dictionary.before_request
@login_required
def before_request():
    """ Protect all of the admin endpoints. """
    if current_user.is_authenticated:
        pass
    else:
        return redirect(url_for('auth.login'))


@dictionary.route('/dictionary')
def index():
    return render_template('pages/dictionary/index.html', dictionaries=current_user.dictionaries)


@dictionary.route('/dictionary', methods=['POST'])
def dictionary_post():
    _json = request.json
    word_id = _json['word_id']
    user_id = current_user.id

    response = service.dictionary_post(user_id, word_id)
    if response:
        return jsonify(status="Success"), 201

    return jsonify(message='Already exist!', status="Error"), 400

# @dictionary.route('/dictionary', methods=['POST'])
# def dictionary_get():
#
#     return jsonify(current_user.dictionaries)
