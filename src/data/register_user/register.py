from typing import Type, Dict
from src.domain.use_cases.register_user import (
    RegisterUser as RegisterUserInterface,
)
from src.data.interfaces import UserRepositoryInterface
from src.domain.models import Users


class RegisterUser(RegisterUserInterface):
    """Class to define usecase: Register user."""

    def __init__(self, user_repository: Type[UserRepositoryInterface]) -> None:
        """COnstruct."""
        self.user_repository = user_repository

    def register(self, name: str, password: str) -> Dict[bool, Users]:
        """Register user usecase.

        Parameters
        ----------
        name: str
            person name
        password: str
            password of the person
        return: Dict
            Dictionary with information of the process
        """
        response = None
        validate_entry = isinstance(name, str) and isinstance(password, str)

        if validate_entry:
            response = self.user_repository.insert_user(
                name=name, password=password
            )
        else:
            msg = """name and password must be 'str'."""
            raise TypeError(msg)

        return {"Success": validate_entry, "Data": response}
