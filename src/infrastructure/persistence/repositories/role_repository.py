from sqlalchemy import select
from sqlalchemy.orm import Session

from src.domain.repositories.role_repository import IRoleRepository
from src.domain.value_objects.role import Role
from src.infrastructure.persistence.models import RoleORM


class SqlAlchemyRoleRepository(IRoleRepository):
    def __init__(self, session: Session) -> None:
        self.session = session

    def get_by_id(self, role_id: int) -> Role | None:
        stmt = select(RoleORM).where(RoleORM.id == role_id)
        model = self.session.scalar(statement=stmt)
        if not model:
            return None
        return Role(model.name)

    def get_by_name(self, name: str) -> Role | None:
        stmt = select(RoleORM).where(RoleORM.name == name)
        model = self.session.scalar(statement=stmt)
        if not model:
            return None
        return Role(model.name)
