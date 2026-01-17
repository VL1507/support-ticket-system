import bcrypt


class BcryptPasswordHasher:
    @staticmethod
    def hash_password(plain_password: str) -> str:
        return bcrypt.hashpw(
            password=plain_password.encode("utf-8"), salt=bcrypt.gensalt()
        ).decode("utf-8")

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        return bcrypt.checkpw(
            password=plain_password.encode("utf-8"),
            hashed_password=hashed_password.encode("utf-8"),
        )
