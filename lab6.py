from flask import Flask, Blueprint, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Установите реальный секретный ключ

lab6 = Blueprint('lab6', __name__)

users = {}  # Хранилище пользователей: {логин: пароль}
offices = [{"number": i, "tenant": "", "price": 900 + i % 3} for i in range(1, 11)]


# Главная страница офисов
@lab6.route('/lab6/')
def lab():
    if 'login' not in session:
        flash('Пожалуйста, войдите в систему.', 'warning')
        return redirect('/lab6/login/')
    return render_template('lab6/lab6.html')


# API JSON-RPC для офисов
@lab6.route('/lab6/json-rpc-api/', methods=['POST'])
def api():
    data = request.json
    id = data['id']

    # Метод получения информации об офисах
    if data['method'] == 'info':
        return {
            'jsonrpc': '2.0',
            'result': offices,
            'id': id
        }

    login = session.get('login')
    if not login:
        return {
            'jsonrpc': '2.0',
            'error': {'code': 1, 'message': 'Unauthorized'},
            'id': id
        }

    # Метод бронирования офиса
    if data['method'] == 'booking':
        office_number = data['params']
        for office in offices:
            if office['number'] == office_number:
                if office['tenant']:
                    return {
                        'jsonrpc': '2.0',
                        'error': {'code': 2, 'message': 'Already booked'},
                        'id': id
                    }
                office['tenant'] = login
                return {'jsonrpc': '2.0', 'result': 'success', 'id': id}

    # Метод снятия аренды
    if data['method'] == 'cancellation':
        office_number = data['params']
        for office in offices:
            if office['number'] == office_number:
                if not office['tenant']:
                    return {
                        'jsonrpc': '2.0',
                        'error': {'code': 3, 'message': 'Not rented'},
                        'id': id
                    }
                if office['tenant'] != login:
                    return {
                        'jsonrpc': '2.0',
                        'error': {'code': 4, 'message': 'Not your rental'},
                        'id': id
                    }
                office['tenant'] = ""
                return {'jsonrpc': '2.0', 'result': 'success', 'id': id}

    return {
        'jsonrpc': '2.0',
        'error': {'code': -32601, 'message': 'Method not found'},
        'id': id
    }


# Страница авторизации
@lab6.route('/lab6/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        if login in users and users[login] == password:
            session['login'] = login
            flash('Вы успешно вошли в систему!', 'success')
            return redirect('/lab6/')
        flash('Неверный логин или пароль', 'danger')
    return render_template('lab6/login.html')


# Страница регистрации
@lab6.route('/lab6/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        if login in users:
            flash('Пользователь с таким логином уже существует', 'danger')
        else:
            users[login] = password
            flash('Вы успешно зарегистрированы! Теперь вы можете войти.', 'success')
            return redirect('/lab6/login/')
    return render_template('lab6/register.html')


# Выход из системы
@lab6.route('/lab6/logout/')
def logout():
    session.pop('login', None)
    flash('Вы вышли из системы.', 'info')
    return redirect('/lab6/login/')


app.register_blueprint(lab6)

if __name__ == '__main__':
    app.run(debug=True)
