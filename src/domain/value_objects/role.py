from enum import StrEnum


class Role(StrEnum):
    USER = "user"
    SUPPORT = "support"
    ADMIN = "admin"

    @property
    def is_admin(self) -> bool:
        return self is Role.ADMIN

    @property
    def is_support(self) -> bool:
        return self is Role.SUPPORT

    @property
    def is_user(self) -> bool:
        return self is Role.USER
