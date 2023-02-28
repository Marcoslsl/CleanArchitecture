from typing import List
from src.domain.models import Pets
from src.domain.tests import mock_pets
from src.data.interfaces import PetRepositoryInterface


class PetRepositorySpy(PetRepositoryInterface):
    """Spy to  pet repository."""

    def __init__(self) -> None:
        """COnstruct."""
        self.insert_pets_params = {}
        self.select_pets_params = {}

    def insert_pet(
        self, name: str, specie: str, age: int, user_id: int
    ) -> Pets:
        """Spy to all the attributes."""
        self.insert_pets_params["name"] = name
        self.insert_pets_params["specie"] = specie
        self.insert_pets_params["age"] = age
        self.insert_pets_params["user_id"] = user_id

        return mock_pets()

    def select_pet(
        self, user_id: int = None, pet_id: int = None
    ) -> List[Pets]:
        """Spy to all the attributes."""
        self.select_pets_params["user_id"] = user_id
        self.select_pets_params["pet_id"] = pet_id

        return [mock_pets()]
