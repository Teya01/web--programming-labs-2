from flask import Blueprint, render_template, request, redirect, session, current_app
import psycopg2
from psycopg2.extras import RealDictCursor
from werkzeug.security import check_password_hash, generate_password_hash
import _sqlite3
from os import path

lab5 = Blueprint('lab5', __name__)


@lab5.route('/lab5/')
def lab():
    return render_template('lab5/lab5.html', login=session.get('login'))


def db_connect():
    if current_app.config['DB_TYPE'] == 'postgres':
        conn = psycopg2.connect(
            host='127.0.0.1',
            port='5433',
            database='teya_adalinskaya_knowledge_base',
            user='teya_adalinskaya_knowledge_base',
            password='postgres'
        )
        cur = conn.cursor(cursor_factory=RealDictCursor)
    else:
        dir_path = path.dirname(path.realpath(__file__))
        db_path = path.join(dir_path, "database.db")
        conn = _sqlite3.connect(db_path)
        conn.row_factory = _sqlite3.Row
        cur = conn.cursor()
    return conn, cur


def db_close(conn, cur):
    conn.commit()
    cur.close()
    conn.close()


@lab5.route('/lab5/logout')
def logout():
    session.pop('login', None)
    return redirect('/lab5/login')


@lab5.route('/lab5/list')
def list_articles():
    login = session.get('login')
    if not login:
        return redirect('/lab5/login')
    
    conn, cur = db_connect()

    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("SELECT * FROM users WHERE login=%s;", (login,))
    else:
        cur.execute("SELECT * FROM users WHERE login=?;", (login,))
    user = cur.fetchone()

    if not user:
        db_close(conn, cur)
        return redirect('/lab5/login')

    user_id = user["id"]

    # Получаем статьи, сортируем по is_favorite (любимые статьи должны быть первыми)
    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("SELECT * FROM articles WHERE login_id=%s ORDER BY is_favorite DESC;", (user_id,))
    else:
        cur.execute("SELECT * FROM articles WHERE login_id=? ORDER BY is_favorite DESC;", (user_id,))
    articles = cur.fetchall()

    db_close(conn, cur)

    if not articles:
        return render_template('lab5/articles.html', articles=None, message="У вас нет статей. Создайте первую!")
    
    return render_template('lab5/articles.html', articles=articles)


@lab5.route('/lab5/create', methods=['GET', 'POST'])
def create_article():
    login = session.get('login')
    if not login:
        return redirect('/lab5/login')

    if request.method == 'GET':
        return render_template('lab5/create_article.html')

    title = request.form.get('title')
    article_text = request.form.get('article_text')
    is_favorite = True if request.form.get('is_favorite') else False
    is_public = True if request.form.get('is_public') else False

    if not title.strip() or not article_text.strip():
        return render_template('lab5/create_article.html', error="Заполните все поля")

    conn, cur = db_connect()

    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("SELECT * FROM users WHERE login=%s;", (login,))
    else:
        cur.execute("SELECT * FROM users WHERE login=?;", (login,))
    user_id = cur.fetchone()["id"]

    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("INSERT INTO articles (login_id, title, article_text, is_favorite, is_public) VALUES (%s, %s, %s, %s, %s);",
                    (user_id, title, article_text, is_favorite, is_public))
    else:
        cur.execute("INSERT INTO articles (login_id, title, article_text, is_favorite, is_public) VALUES (?, ?, ?, ?, ?);",
                    (user_id, title, article_text, is_favorite, is_public))

    db_close(conn, cur)
    return redirect('/lab5/list')


@lab5.route('/lab5/edit/<int:article_id>', methods=['GET', 'POST'])
def edit_article(article_id):
    login = session.get('login')
    if not login:
        return redirect('/lab5/login')

    conn, cur = db_connect()

    if request.method == 'GET':
        if current_app.config['DB_TYPE'] == 'postgres':
            cur.execute("SELECT * FROM articles WHERE id=%s;", (article_id,))
        else:
            cur.execute("SELECT * FROM articles WHERE id=?;", (article_id,))
        article = cur.fetchone()
        db_close(conn, cur)

        if not article:
            return redirect('/lab5/list')

        return render_template('lab5/edit_article.html', article=article)

    title = request.form.get('title')
    article_text = request.form.get('article_text')
    is_favorite = True if request.form.get('is_favorite') else False
    is_public = True if request.form.get('is_public') else False

    if not title.strip() or not article_text.strip():
        return render_template('lab5/edit_article.html', error="Заполните все поля", article={"id": article_id, "title": title, "article_text": article_text})

    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("UPDATE articles SET title=%s, article_text=%s, is_favorite=%s, is_public=%s WHERE id=%s;",
                    (title, article_text, is_favorite, is_public, article_id))
    else:
        cur.execute("UPDATE articles SET title=?, article_text=?, is_favorite=?, is_public=? WHERE id=?;",
                    (title, article_text, is_favorite, is_public, article_id))

    db_close(conn, cur)
    return redirect('/lab5/list')


@lab5.route('/lab5/delete/<int:article_id>', methods=['POST'])
def delete_article(article_id):
    login = session.get('login')
    if not login:
        return redirect('/lab5/login')

    conn, cur = db_connect()

    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("DELETE FROM articles WHERE id=%s;", (article_id,))
    else:
        cur.execute("DELETE FROM articles WHERE id=?;", (article_id,))

    db_close(conn, cur)
    return redirect('/lab5/list')


@lab5.route('/lab5/users')
def list_users():
    login = session.get('login')
    if not login:
        return redirect('/lab5/login')

    conn, cur = db_connect()

    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("SELECT login FROM users;")
    else:
        cur.execute("SELECT login FROM users;")
    
    users = cur.fetchall()
    db_close(conn, cur)

    return render_template('lab5/list_users.html', users=users)


@lab5.route('/lab5/public_articles')
def public_articles():
    conn, cur = db_connect()

    # Запрашиваем только публичные статьи
    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("SELECT * FROM articles WHERE is_public = TRUE ORDER BY is_favorite DESC;")
    else:
        cur.execute("SELECT * FROM articles WHERE is_public = 1 ORDER BY is_favorite DESC;")
    articles = cur.fetchall()

    db_close(conn, cur)

    if not articles:
        return render_template('lab5/public_articles.html', articles=None, message="Публичных статей нет.")
    
    return render_template('lab5/public_articles.html', articles=articles)


