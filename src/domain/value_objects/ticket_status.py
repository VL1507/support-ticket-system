from dataclasses import dataclass
from typing import Literal, Self, final


@final
@dataclass(frozen=True, slots=True)
class TicketStatus:
    name: Literal["Open", "In Progress", "Rejected", "Close"]
    is_closed: bool

    @classmethod
    def open_status(cls) -> Self:
        return cls(name="Open", is_closed=False)

    @classmethod
    def in_progress_status(cls) -> Self:
        return cls(name="In Progress", is_closed=False)

    @classmethod
    def rejected_status(cls) -> Self:
        return cls(name="Rejected", is_closed=True)

    @classmethod
    def close_status(cls) -> Self:
        return cls(name="close", is_closed=True)
