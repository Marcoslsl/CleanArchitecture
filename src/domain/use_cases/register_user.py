from abc import ABC, abstractmethod
from src.domain.models import Users
from typing import Dict


class RegisterUser(ABC):
    """Interface to register  use case."""

    @abstractmethod
    def register(self, name: str, password: str) -> Dict[bool, Users]:
        """Must implement."""
        raise NotImplementedError("Must be implemented")
