from flask import Blueprint

from src.presentation.decorators import login_required

bp = Blueprint(name="user_tickets", import_name=__name__)


@bp.route("/tickets")
@login_required
def tickets() -> str:
    return "user_tickets"
