from typing import Type, Dict, List
from src.domain.use_cases.register_pet import (
    RegisterPet as RegisterPetInterface,
)
from src.data.interfaces import PetRepositoryInterface
from src.domain.models import Pets, Users
from src.data.find_user import FindUser


class RegisterPet(RegisterPetInterface):
    """RegisterPet."""

    def __init__(
        self,
        pet_repository: Type[PetRepositoryInterface],
        find_user: Type[FindUser],
    ) -> None:
        """Construct."""
        self.pet_repository = pet_repository
        self.find_user = find_user

    def register(
        self,
        name: str,
        specie: str,
        age: int,
        user_information: Dict[int, str],
    ) -> Dict[bool, Pets]:
        """Register pet usecase.

        Parameters
        ----------
        name: str
            Name of the pet
        specie: str
            Specie of the pet
        age: int
            age of the pet
        user_information: Dict
            Information about the owner of the pet
        return: Dict
        """
        response = None
        validate_entry = (
            isinstance(name, str)
            and isinstance(specie, str)
            and isinstance(age, int)
        )
        user = self.__find_user_information(user_information)
        checker = validate_entry and user["Success"]

        if checker:
            response = self.pet_repository.insert_pet(
                name=name,
                specie=specie,
                age=age,
                user_id=user_information["user_id"],
            )

        return {"Success": checker, "Data": response}

    def __find_user_information(
        self, user_information: Dict[int, str]
    ) -> Dict[bool, List[Users]]:
        """Check user info and select user.

        Parameters
        ----------
        user_information: Dict
            Dictionary with user_id and/or user_name
        return: Dict
            Dictionary with the response of find_user use case
        """
        user_found = None
        user_params = user_information.keys()

        if ("user_id" in user_params) and ("user_name" in user_params):
            user_found = self.find_user.by_id_and_name(
                user_information["user_name"], user_information["user_id"]
            )

        elif ("user_id" not in user_params) and ("user_name" in user_params):
            user_found = self.find_user.by_name(user_information["user_name"])

        elif ("user_id" in user_params) and ("user_name" not in user_params):
            user_found = self.find_user.by_id(user_information["user_id"])

        else:
            return {"Success": False, "Data": None}

        return user_found
