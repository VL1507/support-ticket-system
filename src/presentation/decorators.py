from collections.abc import Callable
from functools import wraps
from typing import TYPE_CHECKING, Any, cast

from flask import flash, g, redirect, url_for

if TYPE_CHECKING:
    from src.domain.entities.user import User


def login_required(f: Callable[..., Any]) -> Callable[..., Any]:
    """
    Декоратор: требует, чтобы пользователь был авторизован.
    Если нет — перенаправляет на страницу логина.
    """

    @wraps(f)
    def decorated_function(*args: Any, **kwargs: Any) -> Any:
        # Приводим g.user к нужному типу (мы уверены, что он User | None)
        user: User | None = cast("User | None", g.get("user"))

        if user is None:
            flash("Для доступа необходимо войти в систему", "warning")
            return redirect(url_for("auth.login"))

        return f(*args, **kwargs)

    return decorated_function


def admin_required(f: Callable[..., Any]) -> Callable[..., Any]:
    """
    Декоратор: требует, чтобы пользователь был авторизован И имел роль администратора.
    """

    @wraps(f)
    def decorated_function(*args: Any, **kwargs: Any) -> Any:
        user: User | None = cast("User | None", g.get("user"))

        if user is None:
            flash("Войдите в систему", "warning")
            return redirect(url_for("auth.login"))

        if not user.role.is_admin:
            flash("Доступ запрещён: нужны права администратора", "danger")
            return redirect(url_for("auth.success"))

        return f(*args, **kwargs)

    return decorated_function
