class DomainError(Exception):
    """Base class for domain exceptions"""


class LoginAlreadyExistsError(DomainError):
    def __init__(self, login: str | None = None) -> None:
        message = (
            f"Login '{login}' already exists"
            if login
            else "Login already exists"
        )
        super().__init__(message)
        self.login = login


class NoRoleWithThisNameInTheDatabaseError(DomainError):
    def __init__(self, role_name: str | None = None) -> None:
        message = (
            f"There is no role with name={role_name} in the database."
            if role_name
            else "There is no role with this name in the database."
        )
        super().__init__(message)
        self.role_name = role_name
