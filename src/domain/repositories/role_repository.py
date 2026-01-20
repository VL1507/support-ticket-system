from abc import abstractmethod
from typing import Protocol

from src.domain.value_objects.role import Role


class IRoleRepository(Protocol):
    @abstractmethod
    def get_by_id(self, role_id: int) -> Role | None:
        pass

    @abstractmethod
    def get_by_name(self, name: str) -> Role | None:
        pass
