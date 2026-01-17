from flask import Flask

from . import auth_views, home, support_tickets
from .user.init_bp import init_bp as user_init_bp


def init_bp(app: Flask) -> None:
    app.register_blueprint(auth_views.auth_bp)
    app.register_blueprint(home.bp)
    app.register_blueprint(support_tickets.bp, url_prefix="/support")
    user_init_bp(app=app)
