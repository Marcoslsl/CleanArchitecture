from typing import Type, List, Dict
from src.domain.models import Users
from src.domain.use_cases import FindUser as FindUserInterface
from src.data.interfaces import UserRepositoryInterface


class FindUser(FindUserInterface):
    """Class to difine use case find user."""

    def __init__(self, user_repository: Type[UserRepositoryInterface]) -> None:
        """Construct."""
        self.user_repository = user_repository

    def by_id(self, user_id: int) -> Dict[bool, List[Users]]:
        """Select user by id.

        Parameters
        ----------
        user_id: int
            id of the user
        return: Dict
            Dictonary with information of the process
        """
        response = None
        validate_entry = isinstance(user_id, int)

        if validate_entry:
            response = self.user_repository.select_user(user_id=user_id)

        return {"Success": validate_entry, "Data": response}

    def by_name(self, name: str) -> Dict[bool, List[Users]]:
        """Select user by id.

        Parameters
        ----------
        name: str
            name of the user
        return: Dict
            Dictonary with information of the process
        """
        response = None
        validate_entry = isinstance(name, str)

        if validate_entry:
            response = self.user_repository.select_user(name=name)

        return {"Success": validate_entry, "Data": response}

    def by_id_and_name(
        self, name: str, user_id: int
    ) -> Dict[bool, List[Users]]:
        """Select user by id and name.

        Parameters
        ----------
        name: str
            name of the user
        user_id: int
            id of the user
        return: Dict
            Dictonary with information of the process
        """
        response = None
        validate_entry = isinstance(name, str) and isinstance(user_id, int)

        if validate_entry:
            response = self.user_repository.select_user(
                user_id=user_id, name=name
            )

        return {"Success": validate_entry, "Data": response}
