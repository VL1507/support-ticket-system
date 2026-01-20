from dataclasses import dataclass

from src.domain.value_objects.role import Role
from src.domain.value_objects.user_id import UserID


@dataclass
class User:
    id: UserID
    name: str
    login: str
    hash_password: str
    role: Role = Role.USER
    is_active: bool = True
