from flask import Blueprint, flash, redirect, render_template, url_for
from werkzeug.wrappers.response import Response

from src.presentation.decorators import user_required
from src.presentation.forms.create_ticket import CreateTicketForm

bp = Blueprint(
    name="user_tickets_create", import_name=__name__, url_prefix="/tickets"
)


@bp.route("/create", methods=["GET", "POST"])
@user_required
def create() -> Response | str:
    form = CreateTicketForm()

    # Загружаем категории один раз
    # form.category.choices = [
    #     (c.id, c.name)
    #     for c in TicketCategory.query.order_by(TicketCategory.name).all()
    # ]

    if form.validate_on_submit():
        # status_new = TicketStatus.query.filter_by(
        #     name="Новый"
        # ).first()  # или по коду

        # ticket = Ticket(
        #     title=form.title.data,
        #     user_id=current_user.id,
        #     ticket_category_id=form.category.data,
        #     ticket_status_id=status_new.id,
        #     # description хранится обычно в отдельной таблице Message / Comment
        # )
        # db.session.add(ticket)
        # db.session.flush()  # получаем ticket.id

        # Сохраняем первое сообщение
        # first_message = TicketMessage(
        #     ticket_id=ticket.id,
        #     user_id=current_user.id,
        #     content=form.description.data,
        #     is_internal=False,
        # )
        # db.session.add(first_message)

        # db.session.commit()

        flash("Обращение успешно создано!", "success")
        return redirect(
            url_for(
                "user_tickets.ticket",
                # ticket_id=ticket.id
            )
        )

    return render_template("create_ticket.html", form=form)
