from abc import abstractmethod
from typing import Protocol

from src.domain.entities.ticket import Ticket
from src.domain.value_objects.ticket_id import TicketID
from src.domain.value_objects.ticket_status import TicketStatus
from src.domain.value_objects.user_id import UserID


class ITicketRepository(Protocol):
    @abstractmethod
    def get_by_id(self, ticket_id: TicketID) -> Ticket | None: ...

    @abstractmethod
    def save(self, ticket: Ticket) -> None: ...

    @abstractmethod
    def find_by_user(self, user_id: UserID) -> list[Ticket]: ...

    @abstractmethod
    def find_all_open(self) -> list[Ticket]: ...

    @abstractmethod
    def change_status(
        self,
        ticket_id: TicketID,
        new_status: TicketStatus,
        changed_by: UserID,
        comment: str | None = None,
    ) -> bool: ...
