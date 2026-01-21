from argon2 import PasswordHasher, low_level
from argon2.exceptions import (
    InvalidHashError,
    VerificationError,
    VerifyMismatchError,
)

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
        return self.hasher.hash(password=plain_password)

    def verify_password(
        self, plain_password: str, hashed_password: str
    ) -> bool:
        try:
            return self.hasher.verify(
                hash=hashed_password, password=plain_password
            )
        except (
            VerifyMismatchError,
            InvalidHashError,
            VerificationError,
            Exception,
        ):
            return False
