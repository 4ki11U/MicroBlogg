"""Users-reviews forms"""
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, RadioField, SelectField
from wtforms.validators import InputRequired, Length


class Review(FlaskForm):
    """Creating users reviews"""
    category = SelectField('Категория для отзыва',
                           choices=[
                               ('games', 'Игры'),
                               ('films', 'Фильмы'),
                               ('serials', 'Сериалы')
                           ])

    title = StringField('Название проекта',
                        validators=[InputRequired(),
                                    Length(min=2, max=100)])

    description = TextAreaField('Отзыв (ограничение в 1000 символов)',
                                validators=[InputRequired(),
                                            Length(max=1000)])

    mark = RadioField('Поставить оценку',
                      choices=[
                            'Ну такое',
                            'Проходняк (на разок)',
                            'Однознано советую'],
                      validators=[InputRequired()])

    recommend = BooleanField('Рекомендуешь ?', default='checked')
