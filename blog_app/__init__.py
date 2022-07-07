from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask import Flask
from os import path


def start_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'helloworld'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
