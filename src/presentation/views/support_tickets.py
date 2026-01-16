from flask import Blueprint

from src.presentation.decorators import support_required

bp = Blueprint(name="support_tickets", import_name=__name__)


@bp.route("/tickets")
@support_required
def tickets() -> str:
    return "support_tickets"
