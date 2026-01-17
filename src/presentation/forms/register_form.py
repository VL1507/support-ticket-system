from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length


class RegisterForm(FlaskForm):
    name = StringField(
        "Имя",
        validators=[DataRequired(), Length(min=2, max=100)],
        render_kw={"placeholder": "Ваше имя"},
    )
    login = StringField(
        "Логин",
        validators=[DataRequired(), Length(min=3, max=50)],
        render_kw={"placeholder": "Логин"},
    )
    password = PasswordField(
        "Пароль",
        validators=[DataRequired(), Length(min=6)],
        render_kw={"placeholder": "Пароль"},
    )
    password2 = PasswordField(
        "Повторите пароль",
        validators=[DataRequired(), EqualTo("password")],
        render_kw={"placeholder": "Повторите пароль"},
    )
    submit = SubmitField("Зарегистрироваться")
