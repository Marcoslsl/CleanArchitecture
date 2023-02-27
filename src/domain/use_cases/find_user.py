from abc import ABC, abstractmethod
from typing import List, Dict
from src.domain.models import Users


class FindUser(ABC):
    """Interface to finduser use case."""

    @abstractmethod
    def by_id(self, user_id: int) -> Dict[bool, List[Users]]:
        """Must impement."""
        raise NotImplementedError("Must be Implemented.")

    @abstractmethod
    def by_name(self, name: str) -> Dict[bool, List[Users]]:
        """Must impement."""
        raise NotImplementedError("Must be Implemented.")

    @abstractmethod
    def by_id_and_name(
        self, user_id: int, name: str
    ) -> Dict[bool, List[Users]]:
        """Must impement."""
        raise NotImplementedError("Must be Implemented.")
