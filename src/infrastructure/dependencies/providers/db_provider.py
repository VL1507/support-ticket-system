from collections.abc import Iterable

from dishka import Provider, Scope, provide
from sqlalchemy.orm import Session, sessionmaker

from src.config import Config
from src.domain.repositories.role_repository import IRoleRepository
from src.domain.repositories.user_repository import IUserRepository
from src.infrastructure.persistence.repositories.role_repository import (
    SqlAlchemyRoleRepository,
)
from src.infrastructure.persistence.repositories.user_repository import (
    SqlAlchemyUserRepository,
)
from src.infrastructure.persistence.session import new_session_maker


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
