from collections.abc import Iterable

from dishka import Provider, Scope, provide
from sqlalchemy.orm import Session, sessionmaker

from src.application.use_cases.user.login_user import LoginUserUseCase
from src.application.use_cases.user.register_user import RegisterUserUseCase
from src.config import Config
from src.domain.repositories.role_repository import IRoleRepository
from src.domain.repositories.user_repository import IUserRepository
from src.domain.utils.password_hasher import IPasswordHasher
from src.infrastructure.persistence.repositories.role_repository import (
    SqlAlchemyRoleRepository,
)
from src.infrastructure.persistence.repositories.user_repository import (
    SqlAlchemyUserRepository,
)
from src.infrastructure.persistence.session import new_session_maker
from src.infrastructure.security.argon2_password_hasher import (
    Argon2PasswordHasher,
)


class UserUseCasesProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def get_login_user_use_case(
        self,
        user_repo: IUserRepository,
        password_hasher: IPasswordHasher,
    ) -> LoginUserUseCase:
        return LoginUserUseCase(
            user_repo=user_repo, password_hasher=password_hasher
        )

    @provide(scope=Scope.REQUEST)
    def get_register_user_use_case(
        self,
        user_repo: IUserRepository,
        role_repo: IRoleRepository,
        password_hasher: IPasswordHasher,
    ) -> RegisterUserUseCase:
        return RegisterUserUseCase(
            user_repo=user_repo,
            role_repo=role_repo,
            password_hasher=password_hasher,
        )


class SecurityProvider(Provider):
    @provide(scope=Scope.APP)
    def get_password_hasher(
        self,
    ) -> IPasswordHasher:
        return Argon2PasswordHasher()


class DBProvider(Provider):
    @provide(scope=Scope.APP)
    def get_session_maker(self, config: Config) -> sessionmaker[Session]:
        return new_session_maker(db_config=config.DB)

    @provide(scope=Scope.REQUEST)
    def get_session(
        self, session_maker: sessionmaker[Session]
    ) -> Iterable[Session]:
        with session_maker() as session:
            yield session

    @provide(scope=Scope.REQUEST)
    def get_user_repository(self, session: Session) -> IUserRepository:
        return SqlAlchemyUserRepository(session=session)

    @provide(scope=Scope.REQUEST)
    def get_role_repository(self, session: Session) -> IRoleRepository:
        return SqlAlchemyRoleRepository(session=session)
