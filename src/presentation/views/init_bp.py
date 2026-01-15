from flask import Flask

from . import admin_tickets, auth_views, home, user_tickets


def init_bp(app: Flask) -> None:
    app.register_blueprint(auth_views.auth_bp)
    app.register_blueprint(home.bp)
    app.register_blueprint(admin_tickets.bp, url_prefix="/admin")
    app.register_blueprint(user_tickets.bp)
