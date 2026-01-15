from abc import ABC, abstractmethod

from src.domain.entities.user import User


class UserRepository(ABC):
    @abstractmethod
    def get_by_id(self, user_id: int) -> User | None:
        pass

    @abstractmethod
    def get_by_login(self, login: str) -> User | None:
        pass

    @abstractmethod
    def save(self, user: User) -> None:
        pass
