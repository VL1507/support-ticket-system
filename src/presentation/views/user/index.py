from flask import Blueprint, render_template

from src.presentation.decorators import user_required

bp = Blueprint(
    name="user_tickets_list", import_name=__name__, url_prefix="/tickets"
)


@bp.route("/")
@user_required
def tickets() -> str:
    # tickets = []
    return render_template(
        "user_tickets.html",
        #    tickets=tickets
    )
