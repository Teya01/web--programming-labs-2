from flask import Blueprint, render_template, request, redirect
from flask_login import current_user

lab8 = Blueprint('lab8', __name__)

@lab8.route('/lab8/')
def main():
    login = 'anonymous'
    return render_template('lab8/index.html', login=login)

