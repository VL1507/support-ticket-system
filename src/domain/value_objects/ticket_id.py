from dataclasses import dataclass
from typing import Self, final
from uuid import UUID, uuid4


@final
@dataclass(frozen=True, slots=True, eq=True)
class TicketID:
    value: UUID

    @classmethod
    def new(cls) -> Self:
        return cls(value=uuid4())

    @classmethod
    def from_str(cls, s: str) -> Self:
        return cls(UUID(s))
