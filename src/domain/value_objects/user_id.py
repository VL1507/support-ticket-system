from dataclasses import dataclass
from uuid import UUID, uuid4


@dataclass(frozen=True)
class UserID:
    value: UUID

    @classmethod
    def new(cls) -> "UserID":
        return cls(value=uuid4())
