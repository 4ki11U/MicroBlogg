from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from . import db
from .models import Users

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")

        user = Users.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in!", category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Password is incorrect.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("auth/login.html", user=current_user)


@auth.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get("email")
        username = request.form.get("username")
        password = request.form.get("password")
        password_again = request.form.get("password_again")

        email_exists = Users.query.filter_by(email=email).first()
        username_exists = Users.query.filter_by(username=username).first()

        if email_exists:
            flash('Email is already in use.', category='error')
        elif username_exists:
            flash('Username is already in use.', category='error')
        elif password != password_again:
            flash('Password don\'t match!', category='error')
        elif len(username) < 1:
            flash('Username is too short.', category='error')
        elif len(password) < 1:
            flash('Password is too short.', category='error')
        elif len(email) < 1:
            flash("Email is invalid.", category='error')
        else:
            new_user = Users(email=email,
                             username=username,
                             password=generate_password_hash(password, method='sha256')
                             )
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Users created!')
            return redirect(url_for('views.home'))

    return render_template("auth/register.html", user=current_user)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("views.home"))
