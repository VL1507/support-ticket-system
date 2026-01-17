from typing import Protocol


class PasswordHasher(Protocol):
    @staticmethod
    def hash_password(plain_password: str) -> str: ...

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool: ...
