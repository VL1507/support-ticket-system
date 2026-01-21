import bcrypt

from src.domain.utils.password_hasher import IPasswordHasher


class BcryptPasswordHasher(IPasswordHasher):
    def hash_password(self, plain_password: str) -> str:
        return bcrypt.hashpw(
            password=plain_password.encode("utf-8"), salt=bcrypt.gensalt()
        ).decode("utf-8")

    def verify_password(
        self, plain_password: str, hashed_password: str
    ) -> bool:
        return bcrypt.checkpw(
            password=plain_password.encode("utf-8"),
            hashed_password=hashed_password.encode("utf-8"),
        )
