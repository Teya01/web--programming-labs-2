from flask import Blueprint, render_template, request, redirect, url_for, session

lab9 = Blueprint('lab9', __name__)

@lab9.route('/lab9/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        session['name'] = request.form['name']
        return redirect(url_for('.age'))
    return render_template('lab9/index.html')

@lab9.route('/lab9/age/', methods=['GET', 'POST'])
def age():
    if request.method == 'POST':
        session['age'] = int(request.form['age'])
        return redirect(url_for('.gender'))
    return render_template('lab9/age.html')

@lab9.route('/lab9/gender/', methods=['GET', 'POST'])
def gender():
    if request.method == 'POST':
        session['gender'] = request.form['gender']
        return redirect(url_for('.question1'))
    return render_template('lab9/gender.html')

@lab9.route('/lab9/question1/', methods=['GET', 'POST'])
def question1():
    if request.method == 'POST':
        session['preference'] = request.form['preference']
        return redirect(url_for('.question2'))
    return render_template('lab9/question1.html')

@lab9.route('/lab9/question2/', methods=['GET', 'POST'])
def question2():
    if request.method == 'POST':
        session['detail'] = request.form['detail']
        return redirect(url_for('.result'))
    return render_template('lab9/question2.html', preference=session.get('preference'))

@lab9.route('/lab9/result/')
def result():
    name = session.get('name')
    age = session.get('age')
    gender = session.get('gender')
    preference = session.get('preference')
    detail = session.get('detail')

    if preference == 'something_tasty' and detail == 'sweet':
        image = 'candy.jpg'
        message = f"Поздравляю тебя, {name}! Желаю, чтобы ты быстро вырос{'ла' if gender == 'female' else ''}, был{'а' if gender == 'female' else ''} умным{'ой' if gender == 'female' else ''}. Вот тебе подарок — мешочек конфет."
    elif preference == 'something_tasty' and detail == 'savory':
        image = 'cake.jpg'
        message = f"Поздравляю тебя, {name}! Желаю счастья и успеха! Вот тебе кусочек пирога."
    elif preference == 'something_beautiful' and detail == 'nature':
        image = 'nature.jpg'
        message = f"Поздравляю тебя, {name}! Пусть жизнь будет яркой и красивой, как эта открытка!"
    else:
        image = 'art.jpg'
        message = f"Поздравляю тебя, {name}! Пусть жизнь будет яркой и красивой, как эта открытка!"
    

    return render_template('lab9/result.html', message=message, image=image)

