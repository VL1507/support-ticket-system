from dishka import Provider, Scope, provide

from src.application.use_cases.user.login_user import LoginUserUseCase
from src.application.use_cases.user.register_user import RegisterUserUseCase
from src.domain.repositories.role_repository import IRoleRepository
from src.domain.repositories.user_repository import IUserRepository
from src.domain.utils.password_hasher import IPasswordHasher


class UserUseCasesProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def get_login_user_use_case(
        self,
        user_repo: IUserRepository,
        password_hasher: IPasswordHasher,
    ) -> LoginUserUseCase:
        return LoginUserUseCase(
            user_repo=user_repo, password_hasher=password_hasher
        )

    @provide(scope=Scope.REQUEST)
    def get_register_user_use_case(
        self,
        user_repo: IUserRepository,
        role_repo: IRoleRepository,
        password_hasher: IPasswordHasher,
    ) -> RegisterUserUseCase:
        return RegisterUserUseCase(
            user_repo=user_repo,
            role_repo=role_repo,
            password_hasher=password_hasher,
        )
