from typing import Type, List, Dict
from src.domain.models import Pets
from src.domain.use_cases import FindPet as FindPetInterface
from src.data.interfaces import PetRepositoryInterface


class FindPet(FindPetInterface):
    """Class to difine use case find user."""

    def __init__(self, user_repository: Type[PetRepositoryInterface]) -> None:
        """Construct."""
        self.user_repository = user_repository

    def by_id(self, user_id: int) -> Dict[bool, List[Pets]]:
        """Select Pet by id.

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
            response = self.user_repository.select_pet(user_id=user_id)

        return {"Success": validate_entry, "Data": response}

    def by_pet_id(self, pet_id: int) -> Dict[bool, List[Pets]]:
        """Select Pet by pet_id.

        Parameters
        ----------
        pet_id: int
            id of the pet
        return: Dict
            Dictonary with information of the process
        """
        response = None
        validate_entry = isinstance(pet_id, int)

        if validate_entry:
            response = self.user_repository.select_pet(pet_id=pet_id)

        return {"Success": validate_entry, "Data": response}

    def by_id_and_pet_id(
        self, pet_id: int, user_id: int
    ) -> Dict[bool, List[Pets]]:
        """Select Pet by id and pet id.

        Parameters
        ----------
        pet_id: int
            id of the pet
        user_id: int
            id of the pet
        return: Dict
            Dictonary with information of the process
        """
        response = None
        validate_entry = isinstance(pet_id, int) and isinstance(user_id, int)

        if validate_entry:
            response = self.user_repository.select_pet(
                user_id=user_id, pet_id=pet_id
            )

        return {"Success": validate_entry, "Data": response}
