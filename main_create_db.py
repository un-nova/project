import datetime

from flask import Flask, render_template, request, make_response, session
# noinspection PyUnresolvedReferences
from data import db_session
# noinspection PyUnresolvedReferences
from data.users import User
from forms.user import RegisterForm
from werkzeug.utils import redirect


def main():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
    db_session.global_init("db/blogs.db")

    #
    db_sess = db_session.create_session()
    user = db_sess.query(User).first()
    print(user.name)

    for user in db_sess.query(User).all():
        print(user)


if __name__ == '__main__':
    main()
