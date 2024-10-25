from flask import Blueprint, redirect, url_for
lab1 = Blueprint('lab1', __name__)


@lab1.route("/lab1")
def lab():
    return """
    <!doctype html>
    <html>
        <head>
            <title>НГТУ, ФБ, Лабораторная работа 1</title>
            <link rel="stylesheet" href="''' + url_for('static', filename='lab1/lab1.css') + '''">
        </head>
        <body>
            <header>
                НГТУ, ФБ, Лабораторная работа 1
            </header>

            <h1>Flask — фреймворк для создания веб-приложений на языке программирования Python, 
            использующий набор инструментов Werkzeug, а также шаблонизатор Jinja2. Относится к 
            категории так называемых микрофреймворков — минималистичных каркасов веб-приложений, 
            сознательно предоставляющих лишь самые базовые возможности.</h1>
            <p><a href="/menu">Меню</a></p>

            <h2>Реализованные роуты</h2>
            <ul>
                <li><a href="/lab1/student">Информация о студенте</a></li>
                <li><a href="/lab1/python">О языке Python</a></li>
                <li><a href="/lab1/extra">Искусственный интеллект</a></li>
            </ul>

            <footer>
                &copy; Тэя Адалинская, ФБИ-24, 3 курс, 2024
            </footer>
        </body>
    </html>
    """


@lab1.route('/lab1/oak')
def oak():
    return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1/lab1.css') + '''">
    </head>
    <body>
        <h1>Дуб</h1>
        <img src="''' + url_for('static', filename='lab1/oak.jpg') + '''">
    </body>
</html>
'''


@lab1.route("/lab1/student")
def student():
    return '''
<!doctype html>
<html>
    <head>
        <title>Информация о студенте</title>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1/lab1.css') + '''">
    </head>
    <body>
        <p>ФИО: Адалинская Тэя Валентиновна</p>
        <img src="''' + url_for('static', filename='lab1/nstu_logo.png') + '''" alt="Логотип НГТУ">
    </body>
</html>
'''


@lab1.route("/lab1/python")
def python_info():
    return '''
<!doctype html>
<html>
    <head>
        <title>О языке Python</title>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1/lab1.css') + '''">
    </head>
    <body>
        <p>Python - это интерпретируемый, интерактивный, объектно-ориентированный и высокоуровневый 
        язык программирования общего назначения c динамической строгой типизацией и автоматическим 
        управлением памятью, ориентированный на повышение производительности разработчика, читаемости 
        кода, а также на обеспечение переносимости написанных на нем программ. Задумка по реализации 
        языка появилась в конце 1980-х годов, а разработка его реализации началась в 1989 году сотрудником 
        голландского института CWI Гвидо ван Россумом.</p>
        <p>За выбором названия Python также стоит интересный факт. Гвидо ван Россум был поклонником 
        популярного в то время комедийного шоу BBC «Летающий цирк Монти Пайтона». Поэтому он решил 
        взять название Python для создаваемого языка программирования.</p>
        <img src="''' + url_for('static', filename='lab1/python_code.png') + '''" alt="Python Programming">
    </body>
</html>
'''


# Дополнительный маршрут на выбор студента
@lab1.route("/lab1/extra")
def extra():
    return '''
<!doctype html>
<html>
    <head>
        <title>Искусственный интеллект</title>
    </head>
    <body>
        <p>Искусственный интеллект (ИИ) — это термин, который используют для описания машин, выполняющих 
        когнитивные процессы, подобные человеческим, такие как обучение, понимание, рассуждение и 
        взаимодействие. Он может принимать множество форм, включая техническую инфраструктуру, то есть 
        алгоритмы, часть производственного процесса или продукт конечного пользователя.</p>
        <p>Как обучается искусственный интеллект? ИИ обучается на основе данных с использованием алгоритмов. 
        Модель анализирует эти данные, выявляет закономерности и улучшает свои прогнозы через повторные 
        итерации.</p>
        <img src="''' + url_for('static', filename='lab1/ai_image.jpg') + '''" alt="Artificial Intelligence">
    </body>
</html>
'''
