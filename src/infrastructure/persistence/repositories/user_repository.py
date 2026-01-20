from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from src.domain.entities.user import User
from src.domain.repositories.user_repository import IUserRepository
from src.domain.value_objects.role import Role
from src.domain.value_objects.user_id import UserID
from src.infrastructure.exceptions import ThereIsNoRoleIdNameInTheDatabaseError
from src.infrastructure.persistence import models


class SqlAlchemyUserRepository(IUserRepository):
    def __init__(self, session: Session) -> None:
        self.session = session

    def get_by_id(self, user_id: UserID) -> User | None:
        stmt = select(models.User).where(models.User.id == user_id.value)
        model = self.session.scalar(statement=stmt)
        if not model:
            return None
        return User(
            id=UserID(value=model.id),
            name=model.name,
            login=model.login,
            hash_password=model.hash_password,
            role=Role(model.role.name),
        )

    def get_by_login(self, login: str) -> User | None:
        stmt = select(models.User).where(models.User.login == login)
        model = self.session.scalar(statement=stmt)
        if not model:
            return None
        return User(
            id=UserID(value=model.id),
            name=model.name,
            login=model.login,
            hash_password=model.hash_password,
            role=Role(model.role.name),
            is_active=model.is_active,
        )

    def save(self, user: User) -> None:
        role = self.session.scalar(
            select(models.Role).where(models.Role.name == user.role)
        )
        if role is None:
            raise ThereIsNoRoleIdNameInTheDatabaseError(f"{user.role = }")
        model = models.User(
            id=user.id.value,
            name=user.name,
            login=user.login,
            hash_password=user.hash_password,
            role_id=role.id,
            is_active=user.is_active,
        )
        self.session.add(model)
        self.session.commit()
