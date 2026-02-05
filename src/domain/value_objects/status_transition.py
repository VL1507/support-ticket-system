from dataclasses import dataclass
from datetime import datetime
from typing import final

from src.domain.value_objects.ticket_status import TicketStatus
from src.domain.value_objects.user_id import UserID


@final
@dataclass(frozen=True, slots=True)
class StatusTransition:
    from_status: TicketStatus
    to_status: TicketStatus
    changed_by_id: UserID
    changed_at: datetime
    comment: str | None = None
