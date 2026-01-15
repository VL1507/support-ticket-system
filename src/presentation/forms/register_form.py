from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length


class RegisterForm(FlaskForm):
    name = StringField(
        "Имя", validators=[DataRequired(), Length(min=2, max=100)]
    )
    login = StringField(
        "Логин", validators=[DataRequired(), Length(min=3, max=50)]
    )
    password = PasswordField(
        "Пароль", validators=[DataRequired(), Length(min=6)]
    )
    password2 = PasswordField(
        "Повторите пароль", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Зарегистрироваться")
