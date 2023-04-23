import forma as forma
from flask import Flask, render_template, request, make_response, session
from data import db_session, users
from data.lesson import Lessons
from data.users import User
from forms.user import RegisterForm, LoginForm
from werkzeug.utils import redirect
from flask_login import login_user, LoginManager, login_required, logout_user, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)

aunt = False


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)

    db_session.global_init("db/blogs.db")
    db_sess = db_session.create_session()


@app.route("/")
def index():
    db_sess = db_session.create_session()
    return render_template("index.html")


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            email=form.email.data,
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    global aunt
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            aunt = True
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/fruits')
def exercise_1():
    if aunt == True:
        return render_template("fruits.html", title='illustra')
    else:
        return render_template("index.html", title='illustra', message="Зарегестрируйся на сайте, тобы начать")


@app.route("/test1", methods=['GET', 'POST'])

def test1():
    name = 'Fruits and Vegetables'
    b = [0] * 9
    if request.method == 'POST':
        db_sess = db_session.create_session()
        amount0 = request.form.get('Select0')
        if amount0 == 'banana':
            b[0] = 1
        amount1 = request.form.get('Select1')
        if amount1 == 'apple':
            b[1] = 1
        amount2 = request.form.get('Select2')
        if amount2 == 'plum':
            b[2] = 1
        amount3 = request.form.get('Select3')
        if amount3 == 'peach':
            b[3] = 1
        amount4 = request.form.get('Select4')
        if amount4 == 'pear':
            b[4] = 1
        amount5 = request.form.get('Select5')
        if amount5 == 'cucumber':
            b[5] = 1
        amount6 = request.form.get('Select6')
        if amount6 == 'tomato':
            b[6] = 1
        amount7 = request.form.get('Select7')
        if amount7 == 'potato':
            b[7] = 1
        amount8 = request.form.get('Select8')
        if amount8 == 'orange':
            b[8] = 1
        result = sum(b)
        user = db_sess.query(User.id)
        les = Lessons(
            lesson=name,
            result=result,
            user_id=user
        )
        db_sess.add(les)
        db_sess.commit()
    return render_template('test1.html', form=forma)

@app.route("/test2", methods=['GET', 'POST'])

def test2():
    name = 'Colors'
    b = [0] * 9
    if request.method == 'POST':
        db_sess = db_session.create_session()
        amount0 = request.form.get('Select0')
        if amount0 == 'banana':
            b[0] = 1
        amount1 = request.form.get('Select1')
        if amount1 == 'apple':
            b[1] = 1
        amount2 = request.form.get('Select2')
        if amount2 == 'plum':
            b[2] = 1
        amount3 = request.form.get('Select3')
        if amount3 == 'peach':
            b[3] = 1
        amount4 = request.form.get('Select4')
        if amount4 == 'pear':
            b[4] = 1
        amount5 = request.form.get('Select5')
        if amount5 == 'cucumber':
            b[5] = 1
        amount6 = request.form.get('Select6')
        if amount6 == 'tomato':
            b[6] = 1
        amount7 = request.form.get('Select7')
        if amount7 == 'potato':
            b[7] = 1
        amount8 = request.form.get('Select8')
        if amount8 == 'orange':
            b[8] = 1
        result = sum(b)
        user = db_sess.query(User.id)
        les = Lessons(
            lesson=name,
            result=result,
            user_id=user
        )
        db_sess.add(les)
        db_sess.commit()
    return render_template('test1.html', form=forma)

@app.route("/test3", methods=['GET', 'POST'])

def test3():
    name = 'Animals'
    b = [0] * 9
    if request.method == 'POST':
        db_sess = db_session.create_session()
        amount0 = request.form.get('Select0')
        if amount0 == 'cat':
            b[0] = 1
        amount1 = request.form.get('Select1')
        if amount1 == 'dog':
            b[1] = 1
        amount2 = request.form.get('Select2')
        if amount2 == 'bird':
            b[2] = 1
        amount3 = request.form.get('Select3')
        if amount3 == 'rabbit':
            b[3] = 1
        amount4 = request.form.get('Select4')
        if amount4 == 'fox':
            b[4] = 1
        amount5 = request.form.get('Select5')
        if amount5 == 'monkey':
            b[5] = 1
        amount6 = request.form.get('Select6')
        if amount6 == 'pig':
            b[6] = 1
        amount7 = request.form.get('Select7')
        if amount7 == 'lion':
            b[7] = 1
        amount8 = request.form.get('Select8')
        if amount8 == 'elephant':
            b[8] = 1
        result = sum(b)
        user = db_sess.query(User.id)
        les = Lessons(
            lesson=name,
            result=result,
            user_id=user
        )
        db_sess.add(les)
        db_sess.commit()
    return render_template('test3.html', form=forma)

@app.route('/account')
def account():
    if aunt == True:
        db_sess = db_session.create_session()
        user = db_sess.query(User.id)
        return render_template("account.html", title='illustra',message=db_sess.query(Lessons.result).filter(Lessons.lesson == 'Fruits and Vegetables', Lessons.user_id == user)).first()
    else:
        return render_template("index.html", title='illustra', message="Зарегестрируйся на сайте, тобы начать")

@app.route('/logout')
@login_required
def logout():
    global aunt
    aunt = False
    logout_user()
    return redirect("/")


db_session.global_init("db/blogs.db")

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.10')
