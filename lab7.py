from flask import Flask, Blueprint, render_template, request, jsonify, abort
from datetime import datetime

app = Flask(__name__)

lab7 = Blueprint('lab7', __name__)

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

CURRENT_YEAR = datetime.now().year


def validate_film(film):
    errors = {}

    # Проверка названий
    if not film.get('title') and not film.get('title_ru'):
        errors['title'] = 'Должно быть указано хотя бы одно название (оригинальное или русское).'
    if not film.get('title_ru'):
        errors['title_ru'] = 'Русское название не может быть пустым.'

    # Проверка года
    year = film.get('year')
    if not isinstance(year, int) or not (1895 <= year <= CURRENT_YEAR):
        errors['year'] = f'Год должен быть в диапазоне от 1895 до {CURRENT_YEAR}.'

    # Проверка описания
    description = film.get('description', '').strip()
    if not description:
        errors['description'] = 'Описание не может быть пустым.'
    elif len(description) > 2000:
        errors['description'] = 'Описание не должно превышать 2000 символов.'

    return errors


@lab7.route('/lab7/')
def main():
    return render_template('lab7/index.html')


@lab7.route('/lab7/rest-api/films/', methods=['GET'])
def get_films():
    return jsonify(films)


@lab7.route('/lab7/rest-api/films/<int:id>', methods=['GET'])
def get_film_by_id(id):
    if 0 <= id < len(films):
        return jsonify(films[id])
    abort(404)


@lab7.route('/lab7/rest-api/films/<int:id>', methods=['DELETE'])
def del_film(id):
    if 0 <= id < len(films):
        del films[id]
        return jsonify(''), 204
    abort(404)


@lab7.route('/lab7/rest-api/films/<int:id>', methods=['PUT'])
def put_film(id):
    if not (0 <= id < len(films)):
        abort(404)

    film = request.get_json()
    errors = validate_film(film)
    if errors:
        return jsonify(errors), 400

    if not film['title']:
        film['title'] = film['title_ru']

    films[id] = film
    return jsonify(films[id])


@lab7.route('/lab7/rest-api/films/', methods=['POST'])
def add_film():
    film = request.get_json()
    print(f"Полученные данные: {film}")
    errors = validate_film(film)
    if errors:
        print(f"Ошибки валидации: {errors}")
        return jsonify(errors), 400

    if not film['title']:
        film['title'] = film['title_ru']

    films.append(film)
    return jsonify({"id": len(films) - 1}), 201


app.register_blueprint(lab7)

if __name__ == '__main__':
    app.run(debug=True)

