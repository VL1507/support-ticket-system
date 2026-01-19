from dishka.integrations.flask import FromDishka
from flask import (
    Blueprint,
    flash,
    g,
    redirect,
    render_template,
    session,
    url_for,
)
from werkzeug.wrappers.response import Response

from src.domain.exceptions import (
    LoginAlreadyExistsError,
    NoRoleWithThisNameInTheDatabaseError,
)
from src.domain.services.auth_service import AuthService
from src.presentation.exceptions import NotAllFieldsAreFilledInError
from src.presentation.forms.login_form import LoginForm
from src.presentation.forms.register_form import RegisterForm

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["GET", "POST"])
def register(auth_service: FromDishka[AuthService]) -> str | Response:
    form = RegisterForm()
    if form.validate_on_submit():
        try:
            user = auth_service.register(
                name=form.name.data,
                login=form.login.data,
                password=form.password.data,
            )
            session.permanent = True
            session["user_id"] = user.id
            flash("Регистрация успешна!", "success")
            return redirect(url_for("auth.success"))
        except LoginAlreadyExistsError as e:
            flash(str(e), "danger")
        except NotAllFieldsAreFilledInError as e:
            flash(str(e), "danger")
        except NoRoleWithThisNameInTheDatabaseError as e:
            flash(str(e), "danger")
    return render_template("register.html", form=form)


@auth_bp.route("/login", methods=["GET", "POST"])
def login(auth_service: FromDishka[AuthService]) -> str | Response:
    if g.user:
        return redirect(url_for("auth.success"))
    form = LoginForm()
    if form.validate_on_submit():
        user = auth_service.login(form.login.data, form.password.data)
        if user:
            session.permanent = True
            session["user_id"] = user.id
            flash("Добро пожаловать!", "success")
            if user.role.is_admin:
                return redirect("/admin")
            return redirect(url_for("auth.success"))
        flash("Неверный логин или пароль", "danger")
    return render_template("login.html", form=form)


@auth_bp.route("/logout")
def logout() -> Response:
    session.pop("user_id", None)
    flash("Вы вышли из системы", "info")
    return redirect(url_for("auth.login"))


@auth_bp.route("/success")
def success() -> str | Response:
    if not g.user:
        flash("Пожалуйста, войдите в систему", "warning")
        return redirect(url_for("auth.login"))
    return render_template("success.html")
