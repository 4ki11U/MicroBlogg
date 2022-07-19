from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import current_user

from blog_app import db
from blog_app.database.models import Review
from blog_app.forms.reviews import Review

reviews = Blueprint("reviews", __name__)


@reviews.route("/review-create", methods=['GET', 'POST'])
def review_create():
    form = Review()

    if request.method == "POST":
        if form.validate_on_submit():
            project_category = form.title.data
            review = form.description.data

            if not project_category and not review:
                flash('Post cannot be empty', category='error')
            else:
                complete_user_review = Review(
                    category=form.category.data,
                    title_name=form.title.data,
                    description=form.description.data,
                    mark=form.mark.data,
                    recommend=form.recommend.data,
                    author=current_user.id
                )
                try:
                    db.session.add(complete_user_review)
                    db.session.flush()
                    db.session.commit()
                    flash('Отзыв Создан !', category='success')
                except:
                    db.session.rollback()
                    flash('Ошибка добавления в БД', category='error')
                return redirect(url_for('start.home'))
    return render_template("posts/content_create.html", form=form)
