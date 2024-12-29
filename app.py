from flask import Flask, redirect, url_for, render_template
from lab1 import lab1
from lab2 import lab2
from lab3 import lab3
from lab4 import lab4
from lab5 import lab5
from lab6 import lab6
from lab7 import lab7
from lab8 import lab8
from lab9 import lab9
import os
from flask_sqlalchemy import SQLAlchemy
from db import db
from os import path
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'секретно-секретный секрет')
app.config['DB_TYPE'] = os.getenv('DB_TYPE', 'postgres')

if app.config['DB_TYPE'] == 'postgres':
    db_name = 'ivan'
    db_user = 'ivan'
    db_password = '123'
    host_ip = '127.0.0.1'
    host_port = 5433

    app.config['SQLALCHEMY_DATABASE_URI'] = \
        f'postgresql://{db_user}:{db_password}@{host_ip}:{host_port}/{db_name}'
else:
    dir_path = path.dirname(path.realpath(__file__))
    db_path = path.join(dir_path, "ivan.db")
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'

db.init_app(app)

# Инициализация LoginManager
login_manager = LoginManager()


# Укажите маршрут для перенаправления неавторизованных пользователей
login_manager.login_view = 'lab8.login'
login_manager.init_app(app)

# Обработчик для загрузки пользователя
from db.models import users

@login_manager.user_loader
def load_user(login_id):
    return users.query.get(int(login_id))

app.register_blueprint(lab1) 
app.register_blueprint(lab2)
app.register_blueprint(lab3)
app.register_blueprint(lab4)
app.register_blueprint(lab5)
app.register_blueprint(lab6)
app.register_blueprint(lab7)
app.register_blueprint(lab8)
app.register_blueprint(lab9)

@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu", code=302)


@app.route("/menu")
def menu():
    return """
    <!doctype html>
    <html>
        <head>
            <title>НГТУ, ФБ, Лабораторные работы</title>
            <link rel="stylesheet" href="''' + url_for('static', filename='lab1/main.css') + '''">
        </head>
        <body>
            <header>
                НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
            </header>

            <h1>Главная страница</h1>
            <p>Добро пожаловать на сайт!</p>
            <h2>web-сервер на flask</h2>
            <div>
                <ul>
                    <li><a href="/lab1">Первая лабораторная</a></li>
                </ul>
            </div>

            <div>
                <ul>
                    <li><a href="/lab2">Вторая лабораторная</a></li>
                </ul>
            </div>

            <div>
                <ul>
                    <li><a href="/lab3">Третья лабораторная</a></li>
                </ul>
            </div>

            <div>
                <ul>
                    <li><a href="/lab4">Четвёртая лабораторная</a></li>
                </ul>
            </div>

            <div>
                <ul>
                    <li><a href="/lab5">Пятая лабораторная</a></li>
                </ul>
            </div>

            <div>
                <ul>
                    <li><a href="/lab6">Шестая лабораторная</a></li>
                </ul>
            </div>

            <div>
                <ul>
                    <li><a href="/lab7">Седьмая лабораторная</a></li>
                </ul>
            </div>

            <div>
                <ul>
                    <li><a href="/lab8">Восьмая лабораторная</a></li>
                </ul>
            </div>

            <div>
                <ul>
                    <li><a href="/lab9">Девятая лабораторная</a></li>
                </ul>
            </div>
            <footer>
                &copy; Тэя Адалинская, ФБИ-24, 3 курс, 2024
            </footer>
        </body>
    </html>
    """


# Обработчик ошибки 400
@app.errorhandler(400)
def bad_request(error):
    return f'''
    <!doctype html>
    <html>
        <body>
            <h1>Ошибка 400</h1>
            <p>{error.description}</p>
            <a href="{url_for('lab2.all_flowers')}">Вернуться к списку цветов</a>
        </body>
    </html>
    ''', 400

