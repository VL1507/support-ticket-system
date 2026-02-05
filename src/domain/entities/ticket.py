from dataclasses import dataclass, field
from datetime import UTC, datetime

from src.domain.entities.message import Message
from src.domain.entities.user import User
from src.domain.value_objects.status_transition import StatusTransition
from src.domain.value_objects.ticket_category import TicketCategory
from src.domain.value_objects.ticket_id import TicketID
from src.domain.value_objects.ticket_status import TicketStatus
from src.domain.value_objects.user_id import UserID


@dataclass(slots=True)
class Ticket:
    id: TicketID
    title: str
    user_id: UserID
    status: TicketStatus
    category: TicketCategory
    created_at: datetime
    updated_at: datetime
    resolution: str | None = None
    closed_at: datetime | None = None

    messages: list[Message] = field(default_factory=list)

    status_history: list[StatusTransition] = field(default_factory=list)

    def add_message(self, author: User, text: str) -> Message:
        msg = Message.create(ticket_id=self.id, user_id=author.id, text=text)
        self.messages.append(msg)
        self.updated_at = datetime.now(tz=UTC)
        return msg
