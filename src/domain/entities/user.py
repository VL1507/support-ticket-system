from dataclasses import dataclass

from src.domain.value_objects.role import Role


@dataclass
class User:
    id: int | None = None
    name: str = ""
    login: str = ""
    hash_password: str = ""
    role: Role = Role.USER
    is_active: bool = True

    @classmethod
    def create(
        cls, name: str, login: str, hash_password: str, role: Role
    ) -> "User":
        return cls(
            name=name,
            login=login,
            hash_password=hash_password,
            role=role,
            is_active=True,
        )

    def get_id(self) -> str:
        if self.id is None:
            raise ValueError("User has no ID")
        return str(self.id)
