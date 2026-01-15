from flask import Blueprint

from src.presentation.decorators import admin_required, login_required

bp = Blueprint(name="tickets", import_name=__name__)


@bp.route("/my_tickets")
@login_required
def my_tickets() -> str:
    return "my_tickets"


@bp.route("/all_tickets")
@admin_required
def all_tickets() -> str:
    return "all_tickets"
