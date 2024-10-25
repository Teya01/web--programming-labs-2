from flask import Blueprint, render_template, request, make_response, redirect
lab3 = Blueprint('lab3', __name__)


@lab3.route('/lab3/')
def lab():
    name = request.cookies.get('name', 'аноним')
    name_color = request.cookies.get('name_color')
    age = request.cookies.get('age', 'неизвестен')

    return render_template('lab3/lab3.html', name=name, name_color=name_color, age=age)


@lab3.route('/lab3/cookie')
def cookie():
    resp = make_response(redirect('/lab3/'))
    resp.set_cookie('name', 'Alex', max_age=5)
    resp.set_cookie('age', '20')
    resp.set_cookie('name_color', 'magenta')
    return resp


@lab3.route('/lab3/del_cookie')
def del_cookie():
    resp = make_response(redirect('/lab3/'))
    resp.delete_cookie('name')
    resp.delete_cookie('age')
    resp.delete_cookie('name_color')
    return resp


@lab3.route('/lab3/form1')
def form1():
    errors = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле!'
    
    age = request.args.get('age')
    if age == '':
        errors['age'] = 'Заполните поле!'

    age = request.args.get('age')
    sex = request.args.get('sex')
    return render_template('lab3/form1.html', user=user, age=age, sex=sex, errors=errors)


@lab3.route('/lab3/order')
def order():
    return render_template('lab3/order.html')


@lab3.route('/lab3/pay')
def pay():
    price = 0
    drink = request.args.get('drink')
    # Пусть кофе стоит 120 рублей, чёрный чай - 80 рублей, зелёный - 70 рублей
    if drink == 'coffee':
        price = 120
    elif drink == 'black-tea':
        price = 80
    else:
        price = 70

    # Добавить молока удорожает напиток на 30 рублей, а сахара - на 10
    if request.args.get('milk') == 'on':
        price += 30
    if request.args.get('sugar') == 'on':
        price += 10

    return render_template('lab3/pay.html', price=price)

@lab3.route('/lab3/success')
def success():
    price = request.args.get('price', 0)
    return render_template('lab3/success.html', price=price)


@lab3.route('/lab3/clear_settings')
def clear_settings():
    resp = make_response(redirect('/lab3/settings'))
    resp.delete_cookie('color')
    resp.delete_cookie('background')
    resp.delete_cookie('font_size')
    resp.delete_cookie('text_style')
    return resp


@lab3.route('/lab3/settings', methods=['GET', 'POST'])
def settings():
    if request.method == 'POST':
        color = request.form.get('color')
        background = request.form.get('background')
        font_size = request.form.get('font_size')
        text_style = request.form.get('text_style')

        # Устанавливаем куки
        resp = make_response(redirect('/lab3/settings'))
        if color:
            resp.set_cookie('color', color)
        if background:
            resp.set_cookie('background', background)
        if font_size:
            resp.set_cookie('font_size', font_size)
        if text_style:
            resp.set_cookie('text_style', text_style)
        return resp

    # Отображаем настройки, используя куки
    return render_template('lab3/settings.html', 
                           color=request.cookies.get('color', '#000000'), 
                           background=request.cookies.get('background', '#ffffff'), 
                           font_size=request.cookies.get('font_size', '16'), 
                           text_style=request.cookies.get('text_style', ''))


@lab3.route('/lab3/ticket_form', methods=['GET', 'POST'])
def ticket():
    if request.method == 'POST':
        # Получение данных формы
        name = request.form.get('name')
        seat_type = request.form.get('seat_type')
        bedding = request.form.get('bedding') == 'on'
        baggage = request.form.get('baggage') == 'on'
        insurance = request.form.get('insurance') == 'on'
        age = request.form.get('age')
        departure = request.form.get('departure')
        destination = request.form.get('destination')
        travel_date = request.form.get('travel_date')

        # Проверка заполненности полей
        errors = {}
        if not name or not seat_type or not age or not departure or not destination or not travel_date:
            errors['empty'] = "Все поля должны быть заполнены"
        
        # Проверка возраста
        try:
            age = int(age)
            if age < 1 or age > 120:
                errors['age'] = "Возраст должен быть от 1 до 120 лет"
        except ValueError:
            errors['age'] = "Возраст должен быть числом"

        # Если ошибок нет, вычисляем стоимость и отображаем билет
        if not errors:
            price = 700 if age < 18 else 1000
            if seat_type in ['нижняя', 'нижняя боковая']:
                price += 100
            if bedding:
                price += 75
            if baggage:
                price += 250
            if insurance:
                price += 150
            ticket_type = "Детский билет" if age < 18 else "Взрослый билет"

            return render_template(
                'lab3/ticket.html',
                name=name,
                seat_type=seat_type,
                bedding=bedding,
                baggage=baggage,
                insurance=insurance,
                age=age,
                departure=departure,
                destination=destination,
                travel_date=travel_date,
                price=price,
                ticket_type=ticket_type
            )

        return render_template('lab3/ticket_form.html', errors=errors)

    return render_template('lab3/ticket_form.html')


@lab3.route('/lab3/ticket')
def ticket_form():
    return render_template('lab3/ticket.html')