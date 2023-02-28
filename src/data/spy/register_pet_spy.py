from typing import Type, Dict, List
from src.domain.tests import mock_users, mock_pets
from src.domain.models import Pets, Users


class RegisterPetSpy:
    """Class to define usecase: RegisterPet."""

    def __init__(self, pet_repository: any, find_user: any) -> None:
        """Construct."""
        self.pet_repository = pet_repository
        self.find_user = find_user
        self.register_param = {}

    def register(
        self,
        name: str,
        specie: str,
        age: int,
        user_information: Dict[int, str],
    ) -> Dict[bool, Pets]:
        """Register."""
        self.register_param["name"] = name
        self.register_param["specie"] = specie
        self.register_param["user_information"] = user_information
        self.register_param["age"] = age

        response = None
        validate_entry = (
            isinstance(name, str)
            and isinstance(specie, str)
            and isinstance(age, int)
        )
        user = self.__find_user_information(user_information)
        checker = validate_entry and user["Success"]

        if checker:
            response = mock_pets()

        return {"Success": checker, "Data": response}

    def __find_user_information(
        self, user_information: Dict[int, str]
    ) -> Dict[bool, List[Users]]:
        """Check user info and select user."""
        user_found = None
        user_params = user_information.keys()

        if ("user_id" in user_params) and ("user_name" in user_params):
            user_found = {"Success": True, "Data": mock_users()}

        elif ("user_id" not in user_params) and ("user_name" in user_params):
            user_found = {"Success": True, "Data": mock_users()}

        elif ("user_id" in user_params) and ("user_name" not in user_params):
            user_found = {"Success": True, "Data": mock_users()}

        else:
            return {"Success": False, "Data": None}

        return user_found
