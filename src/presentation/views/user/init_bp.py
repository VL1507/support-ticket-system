from flask import Flask

from . import create, index, ticket_ticket_id


def init_bp(app: Flask) -> None:
    app.register_blueprint(index.bp)
    app.register_blueprint(create.bp)
    app.register_blueprint(ticket_ticket_id.bp)
