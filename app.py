from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu", code=302)

@app.route("/lab1")
def lab1():
    return """
    <!doctype html>
    <html>
        <head>
            <title>НГТУ, ФБ, Лабораторная работа 1</title>
            <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
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

@app.route("/menu")
def menu():
    return """
    <!doctype html>
    <html>
        <head>
            <title>НГТУ, ФБ, Лабораторные работы</title>
            <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
        </head>
        <body>
            <header>
                НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
            </header>

            <h1>web-сервер на flask</h1>
            <div>
                <ul>
                    <li><a href="/lab1">Первая лабораторная</a></li>
                </ul>
            </div>

            <footer>
                &copy; Тэя Адалинская, ФБИ-24, 3 курс, 2024
            </footer>
        </body>
    </html>
    """
@app.route('/lab1/oak')

def oak():
    return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <h1>Дуб</h1>
        <img src="''' + url_for('static', filename='oak.jpg') + '''">
    </body>
</html>
'''
@app.route("/lab1/student")
def student():
    return '''
<!doctype html>
<html>
    <head>
        <title>Информация о студенте</title>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <p>ФИО: Адалинская Тэя Валентиновна</p>
        <img src="''' + url_for('static', filename='nstu_logo.png') + '''" alt="Логотип НГТУ">
    </body>
</html>
'''

@app.route("/lab1/python")
def python_info():
    return '''
<!doctype html>
<html>
    <head>
        <title>О языке Python</title>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
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
        <img src="''' + url_for('static', filename='python_code.png') + '''" alt="Python Programming">
    </body>
</html>
'''

# Дополнительный маршрут на выбор студента
@app.route("/lab1/extra")
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
        <img src="''' + url_for('static', filename='ai_image.jpg') + '''" alt="Artificial Intelligence">
    </body>
</html>
'''

@app.route('/lab2/a')
def a():
    return 'без слэша'

@app.route('/lab2/a/')
def a2():
    return 'со слэшем'

from flask import Flask, redirect, url_for, render_template, abort

app = Flask(__name__)

# Изначальный список цветов
flower_list = ['роза', 'тюльпан', 'незабудка', 'ромашка']

# Вывод конкретного цветка
@app.route('/lab2/flowers/<int:flower_id>')
def flowers(flower_id):
    if flower_id >= len(flower_list):
        return "такого цветка нет", 404
    else:
        flower_name = flower_list[flower_id]
        return f'''
        <!doctype html>
        <html>
            <body>
                <h1>Цветок: {flower_name}</h1>
                <a href="{url_for('all_flowers')}">Посмотреть все цветы</a>
            </body>
        </html>
        '''

# Добавление нового цветка с обработкой ошибки 400
@app.route('/lab2/add_flower/')
@app.route('/lab2/add_flower/<name>')
def add_flower(name=None):
    if not name:
        abort(400, description="Вы не задали имя цветка")
    flower_list.append(name)
    return f'''
    <!doctype html>
    <html>
        <body>
            <h1>Добавлен новый цветок</h1>
            <p>Название нового цветка: {name}</p>
            <p>Всего цветов: {len(flower_list)}</p>
            <a href="{url_for('all_flowers')}">Посмотреть все цветы</a>
        </body>
    </html>
    '''

# Вывод всех цветов и их количества
@app.route('/lab2/flowers')
def all_flowers():
    flower_names = ', '.join(flower_list)
    return f'''
    <!doctype html>
    <html>
        <body>
            <h1>Все цветы</h1>
            <p>Количество цветов: {len(flower_list)}</p>
            <p>{flower_names}</p>
            <a href="{url_for('clear_flowers')}">Очистить список</a>
        </body>
    </html>
    '''

# Очистка списка цветов
@app.route('/lab2/clear_flowers')
def clear_flowers():
    flower_list.clear()
    return f'''
    <!doctype html>
    <html>
        <body>
            <h1>Список цветов очищен</h1>
            <a href="{url_for('all_flowers')}">Посмотреть все цветы</a>
        </body>
    </html>
    '''

# Обработчик ошибки 400
@app.errorhandler(400)
def bad_request(error):
    return f'''
    <!doctype html>
    <html>
        <body>
            <h1>Ошибка 400</h1>
            <p>{error.description}</p>
            <a href="{url_for('all_flowers')}">Вернуться к списку цветов</a>
        </body>
    </html>
    ''', 400

@app.route("/")

@app.route('/lab2/example')
def example():
    name, lab_num, group, course = 'Адалинская Тэя', 2, 'ФБИ-24', 3
    fruits = [
        {'name': 'яблоки', 'price': 100},
        {'name': 'груши', 'price': 120},
        {'name': 'апельсины', 'price': 80},
        {'name': 'мандарины', 'price': 95},
        {'name': 'манго', 'price': 321}
    ]
    return render_template('example.html',
                           name=name, lab_num=lab_num, group=group,
                           course=course, fruits=fruits)

@app.route('/lab2/')
def lab2():
    return render_template('lab2.html')

@app.route('/lab2/filters')
def filters():
    phrase = "О <b>сколько</b> <u>нам</u> <i>открытий</i> чудных..."
    return render_template('filter.html', phrase = phrase)

# Выполнение математических операций с двумя числами
@app.route('/lab2/calc/<int:a>/<int:b>')
def calc(a, b):
    try:
        result_sum = a + b
        result_sub = a - b
        result_mul = a * b
        result_div = a / b if b != 0 else 'деление на ноль невозможно'
        result_pow = a ** b
        return f'''
        <!doctype html>
        <html>
            <body>
                <h1>Математические операции с {a} и {b}</h1>
                <p>Сложение: {a} + {b} = {result_sum}</p>
                <p>Вычитание: {a} - {b} = {result_sub}</p>
                <p>Умножение: {a} * {b} = {result_mul}</p>
                <p>Деление: {a} / {b} = {result_div}</p>
                <p>Возведение в степень: {a} ** {b} = {result_pow}</p>
            </body>
        </html>
        '''
    except Exception as e:
        return f"Ошибка: {str(e)}", 400

# Перенаправление с /lab2/calc/ на /lab2/calc/1/1
@app.route('/lab2/calc/')
def calc_default():
    return redirect(url_for('calc', a=1, b=1))

# Перенаправление с /lab2/calc/<int:a> на /lab2/calc/a/1
@app.route('/lab2/calc/<int:a>')
def calc_with_one(a):
    return redirect(url_for('calc', a=a, b=1))

if __name__ == "__main__":
    app.run(debug=True)

# Список книг на стороне сервера
books = [
    {'author': 'Лев Толстой', 'title': 'Война и мир', 'genre': 'Драма', 'pages': 1225},
    {'author': 'Фёдор Достоевский', 'title': 'Преступление и наказание', 'genre': 'Драма', 'pages': 671},
    {'author': 'Антон Чехов', 'title': 'Три сестры', 'genre': 'Драма', 'pages': 152},
    {'author': 'Александр Островский', 'title': 'Гроза', 'genre': 'Драма', 'pages': 124},
    {'author': 'Михаил Булгаков', 'title': 'Мастер и Маргарита', 'genre': 'Драма', 'pages': 480},
    {'author': 'Иван Тургенев', 'title': 'Отцы и дети', 'genre': 'Драма', 'pages': 320},
    {'author': 'Александр Грибоедов', 'title': 'Горе от ума', 'genre': 'Драма', 'pages': 225},
    {'author': 'Николай Гоголь', 'title': 'Ревизор', 'genre': 'Драма', 'pages': 145},
    {'author': 'Алексей Толстой', 'title': 'Пётр Первый', 'genre': 'Драма', 'pages': 767},
    {'author': 'Максим Горький', 'title': 'На дне', 'genre': 'Драма', 'pages': 175}
]

# Обработчик для отображения списка книг
@app.route('/lab2/books')
def show_books():
    return render_template('books.html', books=books)

if __name__ == "__main__":
    app.run(debug=True)
