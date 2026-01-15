from flask import Blueprint

from src.presentation.decorators import admin_required

bp = Blueprint(name="admin_tickets", import_name=__name__)


@bp.route("/tickets")
@admin_required
def tickets() -> str:
    return "admin_tickets"
