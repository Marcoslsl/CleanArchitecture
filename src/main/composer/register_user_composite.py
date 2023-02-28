from src.main.interface import RouterInterface
from src.presenters.controllers import RegisterPetController
from src.data.register_user import RegisterUser
from src.infra.repo.user_repository import UserRepository


def register_user_composer() -> RouterInterface:
    """Composing register."""
    repository = UserRepository()
    use_case = RegisterUser(repository)
    register_use_route = RegisterPetController(use_case)

    return register_use_route
