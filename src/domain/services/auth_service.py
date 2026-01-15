from src.domain.entities.user import User
from src.domain.exceptions import (
    LoginAlreadyExistsError,
    NoRoleWithThisNameInTheDatabaseError,
)
from src.domain.repositories.role_repository import RoleRepository
from src.domain.repositories.user_repository import UserRepository


class AuthService:
    def __init__(
        self, user_repo: UserRepository, role_repo: RoleRepository
    ) -> None:
        self.user_repo = user_repo
        self.role_repo = role_repo

    def register(self, name: str, login: str, password: str) -> User:
        if self.user_repo.get_by_login(login):
            raise LoginAlreadyExistsError(login=login)
        role = self.role_repo.get_by_name(name="user")
        if role is None:
            raise NoRoleWithThisNameInTheDatabaseError(role_name="user")
        user = User.create(
            name=name, login=login, password=password, role=role
        )
        self.user_repo.save(user)
        return user

    def login(self, login: str, password: str) -> User | None:
        user = self.user_repo.get_by_login(login)
        if user and user.verify_password(password):
            return user
        return None
