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


# from dataclasses import dataclass
# from typing import Literal


# @dataclass(frozen=True)
# class Role:
# id: int
# name: Literal["user", "support", "admin"]

# @property
# def is_admin(self) -> bool:
#     return self.name == "admin"

# @property
# def is_support(self) -> bool:
#     return self.name == "support"

# @property
# def is_user(self) -> bool:
#     return self.name == "user"
