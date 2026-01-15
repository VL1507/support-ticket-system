from flask import Blueprint, render_template

bp = Blueprint(name="home", import_name=__name__)


@bp.route("/")
def home() -> str:
    return render_template("home.html")
