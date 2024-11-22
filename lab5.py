from flask import Blueprint, render_template, request, redirect, session
import psycopg2

lab5 = Blueprint('lab5', __name__)


@lab5.route('/lab5/')
def lab():
    return render_template('lab5/lab5.html')


@lab5.route('/lab5/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('lab5/register.html')
    login = request.form.get('login')
    password = request.form.get('password')

    if not (login or password):
        return render_template('lab5/register.html', error='Заполните все поля')
    
    conn = psycopg2.connect(
        host = '127.0.0.1',
        port = '5433',
        database = 'teya_adalinskaya_knowledge_base',
        user = 'teya_adalinskaya_knowledge_base',
        password = 'postgres'
    )
    cur = conn.cursor()

    cur.execute(f"SELECT login FROM users WHERE login='{login}';")
    if cur.fetchone():
        cur.close()
        conn.close()
        return render_template('lab5/register.html',
                               error="Такой пользователь уже существует")
    
    cur.execute(f"INSERT INTO users (login, password) VALUES ('{login}', '{password}');")
    conn.commit()
    cur.close()
    conn.close()
    return render_template('lab5/success.html', login=login)


@lab5.route('/lab5/login')
def login():
    return render_template('lab5/login.html')


@lab5.route('/lab5/list')
def list():
    return render_template('lab5/list.html')


@lab5.route('/lab5/create')
def create():
    return render_template('lab5/create.html')
