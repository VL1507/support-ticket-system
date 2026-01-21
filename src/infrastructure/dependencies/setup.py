from dishka.integrations.flask import setup_dishka
from flask import Flask

from src.config import Config

from .container import make_container_di


def setup_di(app: Flask, config: Config) -> None:
    container = make_container_di(config=config)
    setup_dishka(container=container, app=app, auto_inject=True)
