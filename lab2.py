from flask import Blueprint, redirect, url_for, render_template, request
lab2 = Blueprint('lab2', __name__)

@lab2.route('/lab2/a')
def a():
    return 'без слэша'

@lab2.route('/lab2/a/')
def a2():
    return 'со слэшем'

# Список цветов с ценами
flower_list = [
    {'name': 'роза', 'price': 100},
    {'name': 'тюльпан', 'price': 50},
    {'name': 'незабудка', 'price': 30},
    {'name': 'ромашка', 'price': 25}
]

# Обработчик для отображения всех цветов
@lab2.route('/lab2/flowers')
def all_flowers():
    return render_template('lab2/flowers.html', flowers=flower_list)

# Обработчик для добавления нового цветка
@lab2.route('/lab2/add_flower', methods=['POST'])
def add_flower():
    name = request.form.get('name')
    price = request.form.get('price')
    if name and price:
        flower_list.append({'name': name, 'price': int(price)})
    return redirect(url_for('all_flowers'))

# Обработчик для удаления цветка по его номеру
@lab2.route('/lab2/delete_flower/<int:flower_id>')
def delete_flower(flower_id):
    if flower_id < len(flower_list):
        del flower_list[flower_id]
        return redirect(url_for('all_flowers'))
    else:
        return "Такого цветка нет", 404

# Обработчик для удаления всех цветков
@lab2.route('/lab2/clear_flowers')
def clear_flowers():
    flower_list.clear()
    return redirect(url_for('all_flowers'))


@lab2.route('/lab2/example')
def example():
    name, lab_num, group, course = 'Адалинская Тэя', 2, 'ФБИ-24', 3
    fruits = [
        {'name': 'яблоки', 'price': 100},
        {'name': 'груши', 'price': 120},
        {'name': 'апельсины', 'price': 80},
        {'name': 'мандарины', 'price': 95},
        {'name': 'манго', 'price': 321}
    ]
    return render_template('lab2/example.html',
                           name=name, lab_num=lab_num, group=group,
                           course=course, fruits=fruits)

@lab2.route('/lab2/')
def lab():
    return render_template('lab2.html')

@lab2.route('/lab2/filters')
def filters():
    phrase = "О <b>сколько</b> <u>нам</u> <i>открытий</i> чудных..."
    return render_template('lab2/filter.html', phrase = phrase)

# Выполнение математических операций с двумя числами
@lab2.route('/lab2/calc/<int:a>/<int:b>')
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
@lab2.route('/lab2/calc/')
def calc_default():
    return redirect(url_for('calc', a=1, b=1))

# Перенаправление с /lab2/calc/<int:a> на /lab2/calc/a/1
@lab2.route('/lab2/calc/<int:a>')
def calc_with_one(a):
    return redirect(url_for('calc', a=a, b=1))


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
@lab2.route('/lab2/books')
def show_books():
    return render_template('lab2/books.html', books=books)


# Список котиков
cats = [
    {
        'name': 'Барсик',
        'description': 'Милый котик',
        'image': 'lab2/cats:1.jpeg'
    },
    {
        'name': 'Мурзик',
        'description': 'Дружелюбный кот',
        'image': 'lab2/cats:2.jpeg'
    },
    {
        'name': 'Вася',
        'description': 'Активный кот',
        'image': 'lab2/cats:3.jpeg'
    },
    {
        'name': 'Снежок',
        'description': 'Кот-лежебока',
        'image': 'lab2/cats:4.jpeg'
    },
    {
        'name': 'Пушок',
        'description': 'Ласковый кот',
        'image': 'lab2/cats:5.jpeg'
    }
]

# Маршрут для вывода всех котиков
@lab2.route('/lab2/cats')
def show_cats():
    return render_template('lab2/cats.html', cats=cats)

