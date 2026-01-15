from flask import Flask

from . import auth_views, home, tickets


def init_bp(app: Flask) -> None:
    app.register_blueprint(auth_views.auth_bp)
    app.register_blueprint(home.bp)
    app.register_blueprint(tickets.bp)
