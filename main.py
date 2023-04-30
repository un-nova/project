from flask import Flask, render_template, request, make_response, session, g
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
    global idis
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            aunt = True
            idis = user.id
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
        return render_template("index.html", title='illustra', message="Зарегестрируйся на сайте, чтобы начать")


@app.route('/colours')
def exercise_2():
    if aunt == True:
        return render_template("colors.html", title='illustra')
    else:
        return render_template("index.html", title='illustra', message="Зарегестрируйся на сайте, чтобы начать")


@app.route('/animals')
def exercise_3():
    if aunt == True:
        return render_template("animals.html", title='illustra')
    else:
        return render_template("index.html", title='illustra', message="Зарегестрируйся на сайте, чтобы начать")


@app.route('/numbers')
def exercise_4():
    if aunt == True:
        return render_template("numbers.html", title='illustra')
    else:
        return render_template("index.html", title='illustra', message="Зарегестрируйся на сайте, чтобы начать")


@app.route('/family')
def exercise_5():
    if aunt == True:
        return render_template("family.html", title='illustra')
    else:
        return render_template("index.html", title='illustra', message="Зарегестрируйся на сайте, чтобы начать")


@app.route('/drinks')
def exercise_6():
    if aunt == True:
        return render_template("drink.html", title='illustra')
    else:
        return render_template("index.html", title='illustra', message="Зарегестрируйся на сайте, чтобы начать")


@app.route("/test1", methods=['GET', 'POST'])
def test1():
    global result
    global idis
    a = []
    name = 'Fruits and Vegetables'
    b = [0] * 9
    if request.method == 'POST':
        db_sess = db_session.create_session()
        amount0 = request.form.get('Select0')
        if amount0 == 'banana':
            b[0] = 1
        else:
            a.append('banana')
        amount1 = request.form.get('Select1')
        if amount1 == 'apple':
            b[1] = 1
        else:
            a.append('apple')
        amount2 = request.form.get('Select2')
        if amount2 == 'plum':
            b[2] = 1
        else:
            a.append('plum')
        amount3 = request.form.get('Select3')
        if amount3 == 'peach':
            b[3] = 1
        else:
            a.append('peach')
        amount4 = request.form.get('Select4')
        if amount4 == 'pear':
            b[4] = 1
        else:
            a.append('pear')
        amount5 = request.form.get('Select5')
        if amount5 == 'cucumber':
            b[5] = 1
        else:
            a.append('cucumber')
        amount6 = request.form.get('Select6')
        if amount6 == 'tomato':
            b[6] = 1
        else:
            a.append('tomato')
        amount7 = request.form.get('Select7')
        if amount7 == 'potato':
            b[7] = 1
        else:
            a.append('potato')
        amount8 = request.form.get('Select8')
        if amount8 == 'orange':
            b[8] = 1
        else:
            a.append('orange')
        if len(a) == 0:
            a.append('отсутствуют')
        result = sum(b)
        les = Lessons(
            lesson=name,
            result=result,
            user_id=idis
        )
        db_sess.add(les)
        db_sess.commit()
        return render_template('results.html', message=result, message2=', '.join(a))
    return render_template('test1.html')


@app.route("/test2", methods=['GET', 'POST'])
def test2():
    global result
    global idis
    a = []
    name = 'Colors'
    b = [0] * 9
    if request.method == 'POST':
        db_sess = db_session.create_session()
        amount0 = request.form.get('Select0')
        if amount0 == 'white':
            b[0] = 1
        else:
            a.append('white')
        amount1 = request.form.get('Select1')
        if amount1 == 'yellow':
            b[1] = 1
        else:
            a.append('yellow')
        amount2 = request.form.get('Select2')
        if amount2 == 'pink':
            b[2] = 1
        else:
            a.append('pink')
        amount3 = request.form.get('Select3')
        if amount3 == 'black':
            b[3] = 1
        else:
            a.append('black')
        amount4 = request.form.get('Select4')
        if amount4 == 'red':
            b[4] = 1
        else:
            a.append('red')
        amount5 = request.form.get('Select5')
        if amount5 == 'green':
            b[5] = 1
        else:
            a.append('green')
        amount6 = request.form.get('Select6')
        if amount6 == 'blue':
            b[6] = 1
        else:
            a.append('blue')
        amount7 = request.form.get('Select7')
        if amount7 == 'orange':
            b[7] = 1
        else:
            a.append('orange')
        amount8 = request.form.get('Select8')
        if amount8 == 'grey':
            b[8] = 1
        else:
            a.append('grey')
        if len(a) == 0:
            a.append('отсутствуют')
        result = sum(b)
        les = Lessons(
            lesson=name,
            result=result,
            user_id=idis
        )
        db_sess.add(les)
        db_sess.commit()
        return render_template('results.html', message=result, message2=', '.join(a))
    return render_template('test2.html')


@app.route("/test3", methods=['GET', 'POST'])
def test3():
    global result
    global idis
    a = []
    name = 'Animals'
    b = [0] * 9
    if request.method == 'POST':
        db_sess = db_session.create_session()
        amount0 = request.form.get('Select0')
        if amount0 == 'cat':
            b[0] = 1
        else:
            a.append('cat')
        amount1 = request.form.get('Select1')
        if amount1 == 'dog':
            b[1] = 1
        else:
            a.append('dog')
        amount2 = request.form.get('Select2')
        if amount2 == 'bird':
            b[2] = 1
        else:
            a.append('bird')
        amount3 = request.form.get('Select3')
        if amount3 == 'rabbit':
            b[3] = 1
        else:
            a.append('rabbit')
        amount4 = request.form.get('Select4')
        if amount4 == 'fox':
            b[4] = 1
        else:
            a.append('fox')
        amount5 = request.form.get('Select5')
        if amount5 == 'monkey':
            b[5] = 1
        else:
            a.append('monkey')
        amount6 = request.form.get('Select6')
        if amount6 == 'pig':
            b[6] = 1
        else:
            a.append('pig')
        amount7 = request.form.get('Select7')
        if amount7 == 'lion':
            b[7] = 1
        else:
            a.append('lion')
        amount8 = request.form.get('Select8')
        if amount8 == 'elephant':
            b[8] = 1
        else:
            a.append('elephant')
        if len(a) == 0:
            a.append('отсутствуют')
        result = sum(b)
        les = Lessons(
            lesson=name,
            result=result,
            user_id=idis
        )
        db_sess.add(les)
        db_sess.commit()
        return render_template('results.html', message=result, message2=', '.join(a))
    return render_template('test3.html')


@app.route("/test4", methods=['GET', 'POST'])
def test4():
    global result
    global idis
    a = []
    name = 'Numbers'
    b = [0] * 9
    if request.method == 'POST':
        db_sess = db_session.create_session()
        amount0 = request.form.get('Select0')
        if amount0 == 'four':
            b[0] = 1
        else:
            a.append('four')
        amount1 = request.form.get('Select1')
        if amount1 == 'two':
            b[1] = 1
        else:
            a.append('two')
        amount2 = request.form.get('Select2')
        if amount2 == 'five':
            b[2] = 1
        else:
            a.append('five')
        amount3 = request.form.get('Select3')
        if amount3 == 'seven':
            b[3] = 1
        else:
            a.append('seven')
        amount4 = request.form.get('Select4')
        if amount4 == 'nine':
            b[4] = 1
        else:
            a.append('nine')
        amount5 = request.form.get('Select5')
        if amount5 == 'one':
            b[5] = 1
        else:
            a.append('one')
        amount6 = request.form.get('Select6')
        if amount6 == 'eight':
            b[6] = 1
        else:
            a.append('eight')
        amount7 = request.form.get('Select7')
        if amount7 == 'six':
            b[7] = 1
        else:
            a.append('six')
        amount8 = request.form.get('Select8')
        if amount8 == 'three':
            b[8] = 1
        else:
            a.append('three')
        if len(a) == 0:
            a.append('отсутствуют')
        result = sum(b)
        les = Lessons(
            lesson=name,
            result=result,
            user_id=idis
        )
        db_sess.add(les)
        db_sess.commit()
        return render_template('results.html', message=result, message2=', '.join(a))
    return render_template('test4.html')


@app.route("/test5", methods=['GET', 'POST'])
def test5():
    global result
    global idis
    a = []
    name = 'Family'
    b = [0] * 9
    if request.method == 'POST':
        db_sess = db_session.create_session()
        amount0 = request.form.get('Select0')
        if amount0 == 'kin':
            b[0] = 1
        else:
            a.append('kin')
        amount1 = request.form.get('Select1')
        if amount1 == 'mother':
            b[1] = 1
        else:
            a.append('mother')
        amount2 = request.form.get('Select2')
        if amount2 == 'father':
            b[2] = 1
        else:
            a.append('father')
        amount3 = request.form.get('Select3')
        if amount3 == 'daughter':
            b[3] = 1
        else:
            a.append('daughter')
        amount4 = request.form.get('Select4')
        if amount4 == 'son':
            b[4] = 1
        else:
            a.append('son')
        amount5 = request.form.get('Select5')
        if amount5 == 'grandmother':
            b[5] = 1
        else:
            a.append('grandmother')
        amount6 = request.form.get('Select6')
        if amount6 == 'grandfather':
            b[6] = 1
        else:
            a.append('grandfather')
        amount7 = request.form.get('Select7')
        if amount7 == 'sister':
            b[7] = 1
        else:
            a.append('sister')
        amount8 = request.form.get('Select8')
        if amount8 == 'brother':
            b[8] = 1
        else:
            a.append('brother')
        if len(a) == 0:
            a.append('отсутствуют')
        result = sum(b)
        les = Lessons(
            lesson=name,
            result=result,
            user_id=idis
        )
        db_sess.add(les)
        db_sess.commit()
        return render_template('results.html', message=result, message2=', '.join(a))
    return render_template('test5.html')


@app.route("/test6", methods=['GET', 'POST'])
def test6():
    global result
    global idis
    a = []
    name = 'Drinks'
    b = [0] * 9
    if request.method == 'POST':
        db_sess = db_session.create_session()
        amount0 = request.form.get('Select0')
        if amount0 == 'water':
            b[0] = 1
        else:
            a.append('water')
        amount1 = request.form.get('Select1')
        if amount1 == 'milkshake':
            b[1] = 1
        else:
            a.append('milkshake')
        amount2 = request.form.get('Select2')
        if amount2 == 'juice':
            b[2] = 1
        else:
            a.append('juice')
        amount3 = request.form.get('Select3')
        if amount3 == 'milk':
            b[3] = 1
        else:
            a.append('milk')
        amount4 = request.form.get('Select4')
        if amount4 == 'coffee':
            b[4] = 1
        else:
            a.append('coffee')
        amount5 = request.form.get('Select5')
        if amount5 == 'cola':
            b[5] = 1
        else:
            a.append('cola')
        amount6 = request.form.get('Select6')
        if amount6 == 'lemonade':
            b[6] = 1
        else:
            a.append('lemonade')
        amount7 = request.form.get('Select7')
        if amount7 == 'tea':
            b[7] = 1
        else:
            a.append('tea')
        amount8 = request.form.get('Select8')
        if amount8 == 'cocoa':
            b[8] = 1
        else:
            a.append('cocoa')
        if len(a) == 0:
            a.append('отсутствуют')
        result = sum(b)
        les = Lessons(
            lesson=name,
            result=result,
            user_id=idis
        )
        db_sess.add(les)
        db_sess.commit()
        return render_template('results.html', message=result, message2=', '.join(a))
    return render_template('test6.html')


@app.route('/account')
def account():
    global idis
    if aunt == True:
        db_sess = db_session.create_session()
        user_name = db_sess.query(User.name).filter(User.id == idis).first()
        user_email = db_sess.query(User.email).filter(User.id == idis).first()
        fruits = db_sess.query(Lessons.result).filter(Lessons.lesson == 'Fruits and Vegetables',
                                                      Lessons.user_id == idis).first()
        colors = db_sess.query(Lessons.result).filter(Lessons.lesson == 'Colors',
                                                      Lessons.user_id == idis).first()
        animals = db_sess.query(Lessons.result).filter(Lessons.lesson == 'Animals',
                                                       Lessons.user_id == idis).first()
        numbers = db_sess.query(Lessons.result).filter(Lessons.lesson == 'Numbers',
                                                       Lessons.user_id == idis).first()
        family = db_sess.query(Lessons.result).filter(Lessons.lesson == 'Family',
                                                      Lessons.user_id == idis).first()
        drinks = db_sess.query(Lessons.result).filter(Lessons.lesson == 'Drinks',
                                                      Lessons.user_id == idis).first()

        return render_template('profile.html', user_name=' '.join(user_name), user_email=' '.join(user_email), fruits=' '.join(str(fruits)), colors=' '.join(str(colors)),
                               animals=' '.join(str(animals)), numbers=' '.join(str(numbers)), family=' '.join(str(family)), drinks=' '.join(str(drinks)))
    else:
        return render_template("index.html", title='illastra')


@app.route('/result')
def result():
    global result
    if aunt == True:
        return render_template("index.html", title='illastra', message=result)


@app.route('/logout')
@login_required
def logout():
    global aunt
    aunt = False
    logout_user()
    return redirect("/")


db_session.global_init("db/blogs.db")

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
