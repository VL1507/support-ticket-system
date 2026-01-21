from dishka import Provider, Scope, provide

from src.domain.utils.password_hasher import IPasswordHasher
from src.infrastructure.security.argon2_password_hasher import (
    Argon2PasswordHasher,
)


class SecurityProvider(Provider):
    @provide(scope=Scope.APP)
    def get_password_hasher(
        self,
    ) -> IPasswordHasher:
        return Argon2PasswordHasher()
