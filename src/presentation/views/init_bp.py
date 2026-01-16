from flask import Flask

from . import auth_views, home, support_tickets, user_tickets


def init_bp(app: Flask) -> None:
    app.register_blueprint(auth_views.auth_bp)
    app.register_blueprint(home.bp)
    app.register_blueprint(support_tickets.bp, url_prefix="/support")
    app.register_blueprint(user_tickets.bp)
