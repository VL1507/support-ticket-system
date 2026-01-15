from datetime import UTC, datetime
from typing import Any

from flask import g, session

from src.domain.repositories.user_repository import UserRepository


def load_current_user(user_repo: UserRepository) -> None:
    g.user = None
    if "user_id" in session:
        user = user_repo.get_by_id(session["user_id"])
        if user:
            g.user = user
        else:
            session.pop("user_id")


def inject_user() -> dict[str, Any]:
    return {"current_user": g.user, "current_year": datetime.now(UTC).year}
