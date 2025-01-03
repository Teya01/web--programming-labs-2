from flask import Blueprint, render_template, request, redirect, session
lab4 = Blueprint('lab4', __name__)

@lab4.route('/lab4/')
def lab():
    return render_template('lab4/lab4.html')


@lab4.route('/lab4/div-form')
def div_form():
    return render_template('lab4/div-form.html')


@lab4.route('/lab4/div', methods = ['POST'])
def div():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '':
        return render_template('lab4/div.html', error='Оба поля должны быть заполнены!')
    elif x2 == '0':
        return render_template('lab4/div.html', error='Делитель не должен быть равным нулю!')
    x1 = int(x1)
    x2 = int(x2)
    result = x1 / x2
    return render_template('lab4/div.html', x1=x1, x2=x2, result=result)


@lab4.route('/lab4/sum-form')
def sum_form():
    return render_template('lab4/sum-form.html')


@lab4.route('/lab4/sum', methods = ['POST'])
def sum():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '':
        x1 = 0
        x2 = 0
        result = 0
        return render_template('lab4/sum.html', x1=x1, x2=x2, result=result)
    x1 = int(x1)
    x2 = int(x2)
    result = x1 + x2
    return render_template('lab4/sum.html', x1=x1, x2=x2, result=result)


@lab4.route('/lab4/mul-form')
def mul_form():
    return render_template('lab4/mul-form.html')


@lab4.route('/lab4/mul', methods = ['POST'])
def mul():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '':
        x1 = 1
        x2 = 1
        result = 1
        return render_template('lab4/mul.html', x1=x1, x2=x2, result=result)
    x1 = int(x1)
    x2 = int(x2)
    result = x1 * x2
    return render_template('lab4/mul.html', x1=x1, x2=x2, result=result)


@lab4.route('/lab4/min-form')
def min_form():
    return render_template('lab4/min-form.html')


@lab4.route('/lab4/min', methods = ['POST'])
def min():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '':
        return render_template('lab4/min.html', error='Оба поля должны быть заполнены!')
    x1 = int(x1)
    x2 = int(x2)
    result = x1 - x2
    return render_template('lab4/min.html', x1=x1, x2=x2, result=result)


@lab4.route('/lab4/deg-form')
def deg_form():
    return render_template('lab4/deg-form.html')


@lab4.route('/lab4/deg', methods = ['POST'])
def deg():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '':
        return render_template('lab4/deg.html', error='Оба поля должны быть заполнены!')
    elif x1 == '0' and x2 == '0':
        return render_template('lab4/deg.html', error='Оба поля не могут быть равны нулю!')
    x1 = int(x1)
    x2 = int(x2)
    result = x1 ** x2
    return render_template('lab4/deg.html', x1=x1, x2=x2, result=result)


tree_count = 0

@lab4.route('/lab4/tree', methods = ['GET', 'POST'])
def tree():
    global tree_count
    if request.method == 'GET':
        return render_template('lab4/tree.html', tree_count=tree_count)
    
    operation = request.form.get('operation')

    if operation == 'cut' and tree_count > 0:
        tree_count -= 1
    elif operation == 'plant' and tree_count != 10:
        tree_count += 1
    
    return redirect('/lab4/tree')

# Инициализация списка пользователей
users = [
    {'login': 'alex', 'password': '123', 'name': 'Alex Johnson', 'gender': 'Male'},
    {'login': 'bob', 'password': '555', 'name': 'Bob Marley', 'gender': 'Male'},
    {'login': 'teya', 'password': '456', 'name': 'Teya Adalinskaya', 'gender': 'Female'},
    {'login': 'natalie', 'password': '789', 'name': 'Natalie White', 'gender': 'Female'}
]

def is_authorized():
    return 'login' in session

@lab4.route('/lab4/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        new_login = request.form.get('login')
        new_password = request.form.get('password')
        new_name = request.form.get('name')
        new_gender = request.form.get('gender')

        if not all([new_login, new_password, new_name, new_gender]):
            error = "Все поля должны быть заполнены!"
            return render_template('lab4/register.html', error=error)

        if any(user['login'] == new_login for user in users):
            error = "Пользователь с таким логином уже существует!"
            return render_template('lab4/register.html', error=error)

        # Добавляем нового пользователя
        users.lab4end({
            'login': new_login,
            'password': new_password,
            'name': new_name,
            'gender': new_gender
        })
        return redirect('/lab4/login')

    return render_template('lab4/register.html', error=None)

@lab4.route('/lab4/users', methods=['GET', 'POST'])
def user_list():
    if not is_authorized():
        return redirect('/lab4/login')

    login = session['login']
    current_user = next(user for user in users if user['login'] == login)

    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'delete':
            # Удаляем текущего пользователя
            users[:] = [user for user in users if user['login'] != login]
            session.pop('login', None)
            return redirect('/lab4/login')
        elif action == 'update':
            new_name = request.form.get('name')
            new_password = request.form.get('password')
            for user in users:
                if user['login'] == login:
                    user['name'] = new_name
                    user['password'] = new_password
            return redirect('/lab4/users')

    return render_template('lab4/users.html', users=users, current_user=current_user)

@lab4.route('/lab4/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')

        if not login or not password:
            error = 'Не введён логин или пароль'
            return render_template('lab4/login.html', error=error)

        user = next((user for user in users if user['login'] == login and user['password'] == password), None)
        if user:
            session['login'] = login
            return redirect('/lab4/users')
        else:
            error = 'Неверные логин и/или пароль'
            return render_template('lab4/login.html', error=error)

    return render_template('lab4/login.html', error=None)

@lab4.route('/lab4/logout', methods=['POST'])
def logout():
    session.pop('login', None)
    return redirect('/lab4/login')

@lab4.route('/lab4')
def lab4_home():
    return render_template('lab4/home.html')

if __name__ == '__main__':
    lab4.run(debug=True)

@lab4.route('/lab4/refrigerator', methods=['GET', 'POST'])
def refrigerator():
    message = None
    snowflakes = ""

    if request.method == 'POST':
        temp = request.form.get('temperature')

        if temp is None or temp.strip() == "":
            message = "Ошибка: не задана температура"
        else:
            try:
                temp = int(temp)
                if temp < -12:
                    message = "Не удалось установить температуру — слишком низкое значение"
                elif temp > -1:
                    message = "Не удалось установить температуру — слишком высокое значение"
                elif -12 <= temp <= -9:
                    message = f"Установлена температура: {temp}°C"
                    snowflakes = "\u2744\u2744\u2744" 
                elif -8 <= temp <= -5:
                    message = f"Установлена температура: {temp}°C"
                    snowflakes = "\u2744\u2744"  
                elif -4 <= temp <= -1:
                    message = f"Установлена температура: {temp}°C"
                    snowflakes = "\u2744" 
            except ValueError:
                message = "Ошибка: температура должна быть числом"

    return render_template('lab4/refrigerator.html', message=message, snowflakes=snowflakes)

if __name__ == "__main__":
    lab4.run(debug=True)


grain_prices = {
    "ячмень": 12345,
    "овёс": 8522,
    "пшеница": 8722,
    "рожь": 14111
}

@lab4.route('/lab4/grain_order', methods=['GET', 'POST'])
def grain_order():
    if request.method == 'POST':
        grain_type = request.form.get('grain_type')
        weight = request.form.get('weight')

        # Проверка на ошибки
        if not weight:
            error = "Ошибка: не указан вес зерна."
            return render_template('lab4/grain_order.html', error=error)

        try:
            weight = float(weight)
        except ValueError:
            error = "Ошибка: вес должен быть числом."
            return render_template('lab4/grain_order.html', error=error)

        if weight <= 0:
            error = "Ошибка: вес должен быть больше 0."
            return render_template('lab4/grain_order.html', error=error)

        if weight > 500:
            error = "Ошибка: такого объёма зерна сейчас нет в наличии."
            return render_template('lab4/grain_order.html', error=error)

        # Рассчитать сумму заказа
        price_per_ton = grain_prices.get(grain_type)
        if not price_per_ton:
            error = "Ошибка: неверный тип зерна."
            return render_template('lab4/grain_order.html', error=error)

        total_cost = price_per_ton * weight
        discount = 0

        if weight > 50:
            discount = 0.1 
            total_cost *= (1 - discount)

        return render_template('lab4/grain_order.html', 
                               success=True, 
                               grain_type=grain_type, 
                               weight=weight, 
                               total_cost=total_cost, 
                               discount=discount * 100)

    return render_template('lab4/grain_order.html')

if __name__ == '__main__':
    lab4.run(debug=True)

