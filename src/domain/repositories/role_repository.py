from abc import ABC, abstractmethod

from src.domain.value_objects.role import Role


class RoleRepository(ABC):
    @abstractmethod
    def get_by_id(self, role_id: int) -> Role | None:
        pass

    @abstractmethod
    def get_by_name(self, name: str) -> Role | None:
        pass
