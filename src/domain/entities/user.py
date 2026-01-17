from dataclasses import dataclass

import bcrypt

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
        # hashed = bcrypt.hashpw(
        #     password.encode("utf-8"), bcrypt.gensalt()
        # ).decode("utf-8")
        return cls(
            name=name,
            login=login,
            hash_password=hash_password,
            role=role,
            is_active=True,
        )

    # def verify_password(self, password: str) -> bool:
    #     return bcrypt.checkpw(
    #         password.encode("utf-8"), self.hash_password.encode("utf-8")
    #     )

    def get_id(self) -> str:
        if self.id is None:
            raise ValueError("User has no ID")
        return str(self.id)
