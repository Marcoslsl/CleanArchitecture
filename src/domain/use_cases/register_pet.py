from abc import ABC, abstractmethod
from src.domain.models import Pets
from typing import Dict


class RegisterPet(ABC):
    """Interface to register use case."""

    @abstractmethod
    def register(
        self,
        name: str,
        specie: str,
        age: int,
        user_information: Dict[int, str],
    ) -> Dict[bool, Pets]:
        """Must implement."""
        raise NotImplementedError("Must be implemented")
