from typing import Type
from abc import ABC, abstractmethod
from src.presenters.helpers import HttpRequest, HttpResponse


class RouterInterface(ABC):
    """Router."""

    @abstractmethod
    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Must implement."""
        raise NotImplementedError("Must be implemented.")
