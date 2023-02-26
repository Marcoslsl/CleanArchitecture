from typing import List
from abc import ABC, abstractmethod
from src.domain.models import Pets


class PetRepositoryInterface(ABC):
    """Pet repo interface."""

    @abstractmethod
    def insert_pet(
        cls, name: str, specie: str, age: int, user_id: int
    ) -> Pets:
        """Must implement."""
        raise NotImplementedError("Must be implemented")

    @abstractmethod
    def select_pet(cls, pet_id: int = None, user_id: int = None) -> List[Pets]:
        """Must implement."""
        raise NotImplementedError("Must be implemented")
