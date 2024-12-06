from flask import Flask, redirect, url_for, render_template
from lab1 import lab1
from lab2 import lab2
from lab3 import lab3
from lab4 import lab4
from lab5 import lab5

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'секретно-секретный секрет')
app.config['DB_TYPE'] = os.getenv('DB_TYPE', 'postgres')

app.register_blueprint(lab1) 
app.register_blueprint(lab2)
app.register_blueprint(lab3)
app.register_blueprint(lab4)
app.register_blueprint(lab5)

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

