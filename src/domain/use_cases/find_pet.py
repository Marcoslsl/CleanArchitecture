from abc import ABC, abstractmethod
from typing import List, Dict
from src.domain.models import Pets


class FindPet(ABC):
    """Interface to finduser use case."""

    @abstractmethod
    def by_id(self, user_id: int) -> Dict[bool, List[Pets]]:
        """Must impement."""
        raise NotImplementedError("Must be Implemented.")

    @abstractmethod
    def by_pet_id(self, pet_id: int) -> Dict[bool, List[Pets]]:
        """Must impement."""
        raise NotImplementedError("Must be Implemented.")

    @abstractmethod
    def by_id_and_pet_id(
        self, user_id: int, pet_id: int
    ) -> Dict[bool, List[Pets]]:
        """Must impement."""
        raise NotImplementedError("Must be Implemented.")
