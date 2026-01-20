from typing import Protocol


class IPasswordHasher(Protocol):
    def hash_password(self, plain_password: str) -> str: ...

    def verify_password(
        self, plain_password: str, hashed_password: str
    ) -> bool: ...
