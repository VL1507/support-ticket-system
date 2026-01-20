from dishka import make_container
from dishka.integrations.flask import FlaskProvider, setup_dishka
from flask import Flask
from sqlalchemy.orm import scoped_session

from src.config import Config
from src.infrastructure.persistence.repositories.user_repository import (
    SqlAlchemyUserRepository,
)
from src.infrastructure.persistence.session import new_session_maker
from src.ioc import (
    DBProvider,
    SecurityProvider,
    UserUseCasesProvider,
)
from src.presentation.admin import init_admin
from src.presentation.request_handlers import inject_user, load_current_user
from src.presentation.views.init_bp import init_bp


def create_app() -> Flask:
    config = Config()  # type: ignore  # noqa: PGH003

    app = Flask(
        __name__,
        static_folder="./presentation/static",
        template_folder="./presentation/templates",
    )
    app.config["SECRET_KEY"] = config.APP.SECRET_KEY
    app.config["PERMANENT_SESSION_LIFETIME"] = (
        config.APP.PERMANENT_SESSION_LIFETIME
    )

    init_bp(app=app)

    container = make_container(
        DBProvider(),
        UserUseCasesProvider(),
        SecurityProvider(),
        FlaskProvider(),
        context={Config: config},
    )
    setup_dishka(container=container, app=app, auto_inject=True)

    db_session = scoped_session(new_session_maker(config.DB))
    init_admin(app, db_session)

    user_repo = SqlAlchemyUserRepository(
        session=new_session_maker(config.DB)()
    )
    app.before_request(lambda: load_current_user(user_repo=user_repo))
    app.context_processor(inject_user)

    return app
