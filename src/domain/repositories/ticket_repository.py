from abc import ABC, abstractmethod

from src.domain.value_objects.ti import 


class TicketRepository(ABC):
    @abstractmethod
    def get_by_id(self, ticket_id: int) -> Role | None:
        pass

    @abstractmethod
    def get_by_name(self, name: str) -> Role | None:
        pass
