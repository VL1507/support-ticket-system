from src.domain.entities.user import User
from src.domain.exceptions import (
    LoginAlreadyExistsError,
    NoRoleWithThisNameInTheDatabaseError,
)
from src.domain.repositories.role_repository import RoleRepository
from src.domain.repositories.user_repository import UserRepository
from src.domain.services.password_hasher import PasswordHasher


class AuthService:
    def __init__(
        self,
        user_repo: UserRepository,
        role_repo: RoleRepository,
        password_hasher: PasswordHasher,
    ) -> None:
        self.user_repo = user_repo
        self.role_repo = role_repo
        self.password_hasher = password_hasher

    def register(self, name: str, login: str, password: str) -> User:
        if self.user_repo.get_by_login(login):
            raise LoginAlreadyExistsError(login=login)
        role = self.role_repo.get_by_name(name="user")
        if role is None:
            raise NoRoleWithThisNameInTheDatabaseError(role_name="user")
        hash_password = self.password_hasher.hash_password(
            plain_password=password
        )
        user = User.create(
            name=name, login=login, hash_password=hash_password, role=role
        )
        self.user_repo.save(user)
        return user

    def login(self, login: str, password: str) -> User | None:
        user = self.user_repo.get_by_login(login)
        # if user and user.verify_password(password):
        if user and self.password_hasher.verify_password(
            plain_password=password, hashed_password=user.hash_password
        ):
            return user
        return None
