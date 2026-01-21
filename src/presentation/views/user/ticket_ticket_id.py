from uuid import UUID

from flask import Blueprint

from src.presentation.decorators import user_required

bp = Blueprint(
    name="user_tickets_ticket", import_name=__name__, url_prefix="/tickets"
)


@bp.route("/ticket/<uuid:ticket_id>")
@user_required
def ticket(ticket_id: UUID) -> str:
    return f"ticket {ticket_id}"
