from flask import Flask, Blueprint

from . import create, index


def init_bp(app: Flask) -> None:
    # bp = Blueprint(name=)
    # Blueprint.register_blueprint()
    app.register_blueprint(index.bp)
    app.register_blueprint(create.bp)
