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


users = [
    {'login': 'alex', 'password': '123', 'name': 'Alex Johnson', 'gender': 'Male'},
    {'login': 'bob', 'password': '555', 'name': 'Bob Marley', 'gender': 'Male'},
    {'login': 'teya', 'password': '456', 'name': 'Teya Adalinskaya', 'gender': 'Female'},
    {'login': 'natalie', 'password': '789', 'name': 'Natalie White', 'gender': 'Female'}
]


@lab4.route('/lab4/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if 'login' in session:
            authorized = True
            login = session['login']
            # Find the logged-in user
            user = next((user for user in users if user['login'] == login), None)
        else:
            authorized = False
            login = ''
            user = None
        return render_template('lab4/login.html', authorized=authorized, login=login, user=user, error=None)
    
    login = request.form.get('login')
    password = request.form.get('password')

    if not login:
        error = 'Не введён логин'
        return render_template('lab4/login.html', error=error, authorized=False, login=login, user=None)
    if not password:
        error = 'Не введён пароль'
        return render_template('lab4/login.html', error=error, authorized=False, login=login, user=None)
    
    for user in users:
        if login == user['login'] and password == user['password']:
            session['login'] = login
            return redirect('/lab4')
    
    error = 'Неверные логин и/или пароль'
    return render_template('lab4/login.html', error=error, authorized=False, login=login, user=None)


@lab4.route('/lab4/logout', methods=['POST'])
def logout():
    session.pop('login', None)
    return redirect('/lab4/login')

if __name__ == '__main__':
    lab4.run(debug=True)


@lab4.route('/refrigerator', methods=['GET', 'POST'])
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
                    snowflakes = "\u2744\u2744\u2744"  # Three blue snowflakes
                elif -8 <= temp <= -5:
                    message = f"Установлена температура: {temp}°C"
                    snowflakes = "\u2744\u2744"  # Two blue snowflakes
                elif -4 <= temp <= -1:
                    message = f"Установлена температура: {temp}°C"
                    snowflakes = "\u2744"  # One blue snowflake
            except ValueError:
                message = "Ошибка: температура должна быть числом"

    return render_template('refrigerator.html', message=message, snowflakes=snowflakes)

if __name__ == "__main__":
    lab4.run(debug=True)


