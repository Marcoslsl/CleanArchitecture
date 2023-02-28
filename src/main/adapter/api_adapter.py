from typing import Type
from src.main.interface import RouterInterface
from src.presenters.helpers import HttpResponse, HttpRequest


def flask_adapter(request: any, api_route: Type[RouterInterface]) -> any:
    """Adapter."""
    http_request = HttpRequest(body=request.json)
    response = api_route.route(http_request)

    return response
