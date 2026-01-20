from abc import abstractmethod
from typing import Protocol

from src.domain.entities.user import User
from src.domain.value_objects.user_id import UserID


class IUserRepository(Protocol):
    @abstractmethod
    def get_by_id(self, user_id: UserID) -> User | None:
        pass

    @abstractmethod
    def get_by_login(self, login: str) -> User | None:
        pass

    @abstractmethod
    def save(self, user: User) -> None:
        pass
