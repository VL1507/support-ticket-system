from abc import abstractmethod
from typing import Protocol

from src.domain.entities.message import Message
from src.domain.value_objects.ticket_id import TicketID


class IMessageRepository(Protocol):
    @abstractmethod
    def save(self, message: Message) -> None: ...

    @abstractmethod
    def get_by_ticket_id(self, ticket_id: TicketID) -> list[Message]: ...
