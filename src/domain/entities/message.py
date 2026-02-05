from dataclasses import dataclass
from datetime import UTC, datetime
from typing import Self

from src.domain.value_objects.ticket_id import TicketID
from src.domain.value_objects.user_id import UserID


@dataclass
class Message:
    id: int
    ticket_id: TicketID
    user_id: UserID
    text: str
    created_at: datetime

    @classmethod
    def create(cls, ticket_id: TicketID, user_id: UserID, text: str) -> Self:
        return cls(
            id=-1,
            ticket_id=ticket_id,
            user_id=user_id,
            text=text.strip(),
            created_at=datetime.now(tz=UTC),
        )
