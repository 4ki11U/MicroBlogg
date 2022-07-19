from flask import Blueprint, render_template
from flask_login import current_user

from blog_app.database.models import Post, Review

start = Blueprint("start", __name__)


@start.route("/home", methods=['GET', 'POST'])
def home():
    posts = Post.query.all()
    return render_template("home.html", user=current_user, posts=posts)

# @start.route("/home", methods=['GET', 'POST'])
# def home():
#     users_reviews = Review.query.all()
#     return render_template("home.html", user=current_user, posts=users_reviews)