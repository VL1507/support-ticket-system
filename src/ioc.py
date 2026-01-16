from collections.abc import Iterable

from dishka import Provider, Scope, provide
from sqlalchemy.orm import Session, sessionmaker

from src.config import Config
from src.domain.repositories.role_repository import RoleRepository
from src.domain.repositories.user_repository import UserRepository
from src.domain.services.auth_service import AuthService
from src.infrastructure.database.accessor import new_session_maker
from src.infrastructure.repositories.role_repository import (
    SqlAlchemyRoleRepository,
)
from src.infrastructure.repositories.user_repository import (
    SqlAlchemyUserRepository,
)


class AuthProvider(Provider):
    @provide(scope=Scope.APP)
    def get_user_repository_for_auth(
        self, config: Config
    ) -> SqlAlchemyUserRepository:
        with new_session_maker(db_config=config.DB)() as session:
            return SqlAlchemyUserRepository(session=session)


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
    def get_user_repository(self, session: Session) -> UserRepository:
        return SqlAlchemyUserRepository(session=session)

    @provide(scope=Scope.REQUEST)
    def get_role_repository(self, session: Session) -> RoleRepository:
        return SqlAlchemyRoleRepository(session=session)

    @provide(scope=Scope.REQUEST)
    def get_auth_service(
        self, user_repo: UserRepository, role_repo: RoleRepository
    ) -> AuthService:
        return AuthService(user_repo=user_repo, role_repo=role_repo)
