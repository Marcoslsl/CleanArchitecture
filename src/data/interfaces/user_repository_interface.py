from typing import List
from abc import ABC, abstractmethod
from src.domain.models import Users


class UserRepositoryInterface(ABC):
    """Pet repo interface."""

    @abstractmethod
    def insert_user(cls, name: str, password: str) -> Users:
        """Must implement."""
        raise NotImplementedError("Must be implemented")

    @abstractmethod
    def select_user(cls, user_id: int = None, name: str = None) -> List[Users]:
        """Must implement."""
        raise NotImplementedError("Must be implemented")
