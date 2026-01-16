from flask import Blueprint

from src.presentation.decorators import user_required

bp = Blueprint(name="user_tickets", import_name=__name__)


@bp.route("/tickets")
@user_required
def tickets() -> str:
    return "user_tickets"
