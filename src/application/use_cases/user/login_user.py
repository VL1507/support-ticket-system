from src.domain.entities.user import User
from src.domain.repositories.user_repository import IUserRepository
from src.domain.utils.password_hasher import IPasswordHasher


class LoginUserUseCase:
    def __init__(
        self,
        user_repo: IUserRepository,
        password_hasher: IPasswordHasher,
    ) -> None:
        self.user_repo = user_repo
        self.password_hasher = password_hasher

    def __call__(self, login: str, password: str) -> User | None:
        user = self.user_repo.get_by_login(login=login)
        if user and self.password_hasher.verify_password(
            plain_password=password, hashed_password=user.hash_password
        ):
            return user
        return None
