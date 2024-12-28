from flask import Blueprint, render_template, request, jsonify, abort

lab7 = Blueprint('lab7', __name__)

@lab7.route('/lab7/')
def main():
    return render_template('lab7/index.html')


films = [
    {
        "title": "The Intouchables",
        "title_ru": "1+1",
        "year": 2011,
        "description": "Трогательная история невероятной дружбы между парализованным аристократом и его помощником из бедного района Парижа."
    },
    {
        "title": "The Age of Adaline",
        "title_ru": "Век Адалин",
        "year": 2015,
        "description": "Молодая женщина, родившаяся в начале XX века, перестает стареть после загадочной аварии и хранит свою тайну, ведя уединенный образ жизни."
    },
    {
        "title": "The Curious Case of Benjamin Button",
        "title_ru": "Загадочная история Бенджамина Баттона",
        "year": 2008,
        "description": "История мужчины, который рождается стариком и молодеет с годами, проходя необычный жизненный путь, полный любви, потерь и открытий."
    },
]


@lab7.route('/lab7/rest-api/films/', methods=['GET'])
def get_films():
    return jsonify(films)


@lab7.route('/lab7/rest-api/films/<int:id>', methods=['GET'])
def get_film_by_id(id):
    if 0 <= id < len(films):  # Проверка на корректность id
        return jsonify(films[id])
    else:
        abort(404)  # Возврат ошибки 404, если id невалиден


@lab7.route('/lab7/rest-api/films/<int:id>', methods=['DELETE'])
def del_film(id):
    if 0 <= id < len(films):  # Проверка на корректность id
        del films[id]  # Удаление фильма
        return '', 204  # Успешный ответ без содержимого
    else:
        abort(404)  # Возврат ошибки 404, если id невалиден


@lab7.route('/lab7/rest-api/films/<int:id>', methods=['PUT'])
def put_film(id):
    if 0 <= id < len(films):  # Проверка на корректность id
        film = request.get_json()  # Получение данных из тела запроса
        films[id] = film  # Обновление фильма
        return jsonify(films[id])  # Возврат обновленного фильма
    else:
        abort(404)  # Возврат ошибки 404, если id невалиден


