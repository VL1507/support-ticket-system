from sqlalchemy import select
from sqlalchemy.orm import Session

from src.domain.entities.user import User
from src.domain.repositories.user_repository import UserRepository
from src.domain.value_objects.role import Role
from src.infrastructure.database import models


class SqlAlchemyUserRepository(UserRepository):
    def __init__(self, session: Session) -> None:
        self.session = session

    def get_by_id(self, user_id: int) -> User | None:
        stmt = select(models.User).where(models.User.id == user_id)
        model = self.session.scalar(statement=stmt)
        if not model:
            return None
        return User(
            id=model.id,
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
            id=model.id,
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
            raise Exception("Not role in db")
        model = models.User(
            name=user.name,
            login=user.login,
            hash_password=user.hash_password,
            role_id=role.id,
            is_active=user.is_active,
        )
        self.session.add(model)
        self.session.commit()
        self.session.refresh(model)
        user.id = model.id
