from dishka import Container, make_container
from dishka.integrations.flask import FlaskProvider

from src.config import Config

from .providers import DBProvider, SecurityProvider, UserUseCasesProvider


def make_container_di(config: Config) -> Container:
    return make_container(
        DBProvider(),
        UserUseCasesProvider(),
        SecurityProvider(),
        FlaskProvider(),
        context={Config: config},
    )
