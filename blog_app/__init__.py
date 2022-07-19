"""Initialize Flask app."""
from os import path

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DATABASE = r'database/database.db'  # change if need to relocate


def start_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'helloworld'

    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DATABASE}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    from blog_app.routes.start_page import start
    from blog_app.routes.auth.authorization import auth
    from blog_app.routes.reviews.reviews import reviews
    from blog_app.routes.posts.posts import notes

    from blog_app.database.models import Users, Post, Comment, Like, Review

    app.register_blueprint(reviews, url_prefix='/')
    app.register_blueprint(notes, url_prefix='/')
    app.register_blueprint(start, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'authorization.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return Users.query.get(int(id))

    return app


def create_database(app):
    if not path.exists('blog_app' + DATABASE):
        print('Created DATABASE is OK')
        db.create_all(app=app)
