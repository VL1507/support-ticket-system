from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class CreateTicketForm(FlaskForm):
    title = StringField(
        "Тема",
        validators=[
            DataRequired(message="Тема обязательна"),
            Length(
                min=5, max=255, message="Тема должна быть от 5 до 255 символов"
            ),
        ],
        render_kw={
            "autofocus": True,
            "placeholder": "Кратко опишите суть проблемы",
        },
    )

    category = SelectField(
        "Категория",
        coerce=int,
        validators=[DataRequired(message="Выберите категорию")],
    )

    description = TextAreaField(
        "Описание проблемы",
        validators=[
            DataRequired(message="Опишите проблему"),
            Length(
                min=1,
                max=5000,
                message="Описание должно быть от 1 до 5000 символов",
            ),
        ],
        render_kw={
            "rows": 6,
            "placeholder": "Подробно опишите, что произошло, какие шаги привели к проблеме, что вы уже пробовали",
        },
    )

    submit = SubmitField("Создать обращение")
