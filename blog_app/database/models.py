"""Database models."""
from datetime import datetime

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from blog_app import db


class Users(UserMixin, db.Model):
    """General FlaskUsers account model"""
    # __tablename__ = 'flasklogin-users'

    id = db.Column(
        db.Integer,
        primary_key=True
    )
    username = db.Column(
        db.String(100),
        nullable=False,
        unique=True
    )
    email = db.Column(
        db.String(50),
        unique=True,
        nullable=False
    )
    password = db.Column(
        db.String(200),
        primary_key=False,
        unique=False,
        nullable=False
    )
    date_created = db.Column(
        db.DateTime(timezone=True),
        default=datetime.now(),
        unique=False,
        nullable=True
    )
    posts = db.relationship(
        'Post',
        backref='user',
        passive_deletes=True
    )
    comments = db.relationship(
        'Comment',
        backref='user',
        passive_deletes=True
    )
    likes = db.relationship(
        'Like',
        backref='user',
        passive_deletes=True
    )

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password,
                                               method='sha256')

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Review(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    category = db.Column(
        db.Text,
        nullable=False
    )
    title_name = db.Column(
        db.Text,
        nullable=False
    )
    description = db.Column(
        db.Text,
        nullable=False
    )
    mark = db.Column(
        db.Text,
        nullable=False
    )
    recommend = db.Column(
        db.Boolean,
        nullable=False
    )
    date_created = db.Column(
        db.DateTime(timezone=True),
        default=datetime.now()
    )
    author = db.Column(
        db.Integer,
        db.ForeignKey('users.id',
                      ondelete="CASCADE"),
        nullable=False
    )


class Post(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    text = db.Column(
        db.Text,
        nullable=False
    )
    date_created = db.Column(
        db.DateTime(timezone=True),
        default=datetime.now()
    )
    author = db.Column(
        db.Integer,
        db.ForeignKey('users.id',
                      ondelete="CASCADE"),
        nullable=False
    )
    comments = db.relationship(
        'Comment',
        backref='post',
        passive_deletes=True
    )
    likes = db.relationship(
        'Like',
        backref='post',
        passive_deletes=True
    )


class Comment(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    text = db.Column(
        db.String(200),
        nullable=False
    )
    date_created = db.Column(
        db.DateTime(timezone=True),
        default=datetime.now()
    )
    author = db.Column(
        db.Integer,
        db.ForeignKey('users.id',
                      ondelete="CASCADE"),
        nullable=False
    )
    post_id = db.Column(
        db.Integer,
        db.ForeignKey('post.id',
                      ondelete="CASCADE"),
        nullable=False
    )


class Like(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    date_created = db.Column(
        db.DateTime(timezone=True),
        default=datetime.now()
    )
    author = db.Column(
        db.Integer,
        db.ForeignKey(
            'users.id',
            ondelete="CASCADE"),
        nullable=False
    )
    post_id = db.Column(
        db.Integer,
        db.ForeignKey('post.id',
                      ondelete="CASCADE"),
        nullable=False
    )
