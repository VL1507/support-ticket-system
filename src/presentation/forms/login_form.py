from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    login = StringField(
        "Логин",
        validators=[DataRequired()],
        render_kw={"placeholder": "Логин"},
    )
    password = PasswordField(
        "Пароль",
        validators=[DataRequired()],
        render_kw={"placeholder": "Пароль"},
    )
    submit = SubmitField("Войти")
