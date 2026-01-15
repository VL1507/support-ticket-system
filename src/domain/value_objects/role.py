from dataclasses import dataclass


@dataclass(frozen=True)
class Role:
    id: int
    name: str

    @property
    def is_admin(self) -> bool:
        return self.name == "admin"
