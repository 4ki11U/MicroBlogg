from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import login_required, current_user

from blog_app import db
from blog_app.database.models import Post, Users, Comment, Like


notes = Blueprint("posts", __name__, template_folder='templates/posts')


@notes.route("/create-post", methods=['GET', 'POST'])
@login_required
def create_post():
    if request.method == "POST":
        text = request.form.get('text')
        if not text:
            flash('Post cannot be empty', category='error')
        else:
            post = Post(text=text, author=current_user.id)
            try:
                db.session.add(post)
                db.session.flush()
                db.session.commit()
                flash('Post created!', category='success')
            except:
                db.session.rollback()
                print("Ошибка добавления в БД")
            return redirect(url_for('start.home'))

    return render_template('posts/create_post.html', user=current_user)


@notes.route("/delete-post/<id>")
@login_required
def delete_post(id):
    post = Post.query.filter_by(id=id).first()

    if not post:
        flash("Post does not exist.", category='error')
    elif current_user.id != post.author :
        flash('You do not have permission to delete this post.', category='error')
    else:
        db.session.delete(post)
        db.session.commit()
        flash('Post deleted.', category='success')

    return redirect(url_for('start.home'))


@notes.route("/posts/<username>")
@login_required
def posts(username):
    user = Users.query.filter_by(username=username).first()

    if not user:
        flash('No user with that username exists.', category='error')
        return redirect(url_for('start.home'))
    posts = user.posts

    return render_template("posts/posts.html", user=current_user, posts=posts, username=username)


@notes.route("/like-post/<post_id>", methods=['GET', 'POST'])
@login_required
def like(post_id):
    post = Post.query.filter_by(id=post_id).first()
    like = Like.query.filter_by(
        author=current_user.id, post_id=post_id).first()

    if not post:
        return jsonify({'error': 'Post does not exist.'}, 400)
    elif like:
        db.session.delete(like)
        db.session.commit()
    else:
        like = Like(author=current_user.id, post_id=post_id)
        db.session.add(like)
        db.session.commit()

    return jsonify({"likes": len(post.likes), "liked": current_user.id in map(lambda x: x.author, post.likes)})
