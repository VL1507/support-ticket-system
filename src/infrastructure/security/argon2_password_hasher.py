from argon2 import PasswordHasher, low_level
from argon2.exceptions import InvalidHashError, VerifyMismatchError

from src.domain.utils.password_hasher import IPasswordHasher


class Argon2PasswordHasher(IPasswordHasher):
    def __init__(self) -> None:
        super().__init__()
        self.hasher = PasswordHasher(
            time_cost=3,
            memory_cost=64 * 1024,
            parallelism=4,
            type=low_level.Type.ID,
        )

    def hash_password(self, plain_password: str) -> str:
        return self.hasher.hash(plain_password.encode("utf-8"))

    def verify_password(
        self, plain_password: str, hashed_password: str
    ) -> bool:
        try:
            return self.hasher.verify(
                hashed_password, plain_password.encode("utf-8")
            )
        except (VerifyMismatchError, InvalidHashError, Exception):
            return False
