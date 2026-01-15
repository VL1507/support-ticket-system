from flask import Blueprint, render_template

from src.presentation.decorators import admin_required, login_required

bp = Blueprint(name="home", import_name=__name__)


@bp.route("/")
def home() -> str:
    return render_template("home.html")


@bp.route("/user")
@login_required
def test_user() -> str:
    return "Для юзера"


@bp.route("/admin")
@admin_required
def test_admin() -> str:
    return "Для админа"
