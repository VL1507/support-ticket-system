from typing import TYPE_CHECKING, Any, cast

from flask import Flask, flash, g, redirect, url_for
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from sqlalchemy.orm import Session, scoped_session
from werkzeug.wrappers.response import Response

from src.infrastructure.database.models import (
    Message,
    Role,
    Ticket,
    TicketCategory,
    TicketStatus,
    TicketStatusHistory,
    User,
)

if TYPE_CHECKING:
    from src.domain.entities import user as user_entities


class AdminRequiredIndexView(AdminIndexView):
    def is_accessible(self) -> bool:
        user: user_entities.User | None = cast(
            "user_entities.User | None", g.get("user")
        )

        if user is None:
            flash("Войдите в систему", "warning")
            return False

        if not user.role.is_admin:  # твоя проверка из декоратора
            flash("Доступ запрещён: нужны права администратора", "danger")
            return False

        return True

    def inaccessible_callback(self, name: str, **kwargs: Any) -> Response:
        if g.get("user") is None:
            return redirect(url_for("auth.login"))
        return redirect(url_for("auth.success"))


class AdminRequiredModelView(ModelView):
    def is_accessible(self) -> bool:
        user: user_entities.User | None = cast(
            "user_entities.User | None", g.get("user")
        )

        if user is None:
            return False

        return user.role.is_admin

    def inaccessible_callback(self, name: str, **kwargs: Any) -> Response:
        if g.get("user") is None:
            return redirect(url_for("auth.login"))
        return redirect(url_for("auth.success"))


def init_admin(app: Flask, db_session: scoped_session[Session]) -> Admin:
    admin = Admin(
        app,
        name="Техподдержка — Админка",
        url="/admin",
        index_view=AdminRequiredIndexView(),
    )

    admin.add_view(
        AdminRequiredModelView(User, db_session, name="Пользователи")
    )
    admin.add_view(AdminRequiredModelView(Role, db_session, name="Роли"))
    admin.add_view(
        AdminRequiredModelView(Message, db_session, name="Сообщения")
    )
    admin.add_view(
        AdminRequiredModelView(Ticket, db_session, name="Обращения")
    )
    admin.add_view(
        AdminRequiredModelView(
            TicketCategory, db_session, name="Категории обращений"
        )
    )
    admin.add_view(
        AdminRequiredModelView(
            TicketStatus, db_session, name="Статусы обращений"
        )
    )
    admin.add_view(
        AdminRequiredModelView(
            TicketStatusHistory, db_session, name="История статусов обращений"
        )
    )

    return admin
