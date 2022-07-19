"""Sign-up & log-in forms."""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Optional
from wtforms.validators import Length


class SignupForm(FlaskForm):
    """User Sign-up Form."""
    username = StringField(
        'Username',
        validators=[DataRequired()]
    )
    email = StringField(
        'Email',
        validators=[
            Length(min=6),
            Email(message='Enter a valid email.'),
            DataRequired()
        ]
    )
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=6, message='Select a stronger password.')
        ]
    )
    confirm = PasswordField(
        'Confirm Your Password',
        validators=[
            DataRequired(),
            EqualTo('password', message='Passwords must match.')
        ]
    )
    website = StringField('Website',
                          validators=[Optional()]
                          )
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    """User Log-in Form."""
    name = StringField(
        'Username',
        validators=[DataRequired()]
    )
    email = StringField('Email',
                        validators=[DataRequired(),
                                    Email(message='Enter a valid email.')
                                    ]
                        )
    confirm = PasswordField(
        'Confirm Your Password',
        validators=[
            DataRequired(),
            EqualTo('password', message='Passwords must match.')
        ]
    )
    password = PasswordField('Password', validators=[DataRequired()])

    submit = SubmitField('Log In')
