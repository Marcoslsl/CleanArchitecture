from typing import Dict


class HttpRequest:
    """Class to http_request representation."""

    def __init__(
        self, header: Dict = None, body: Dict = None, query: Dict = None
    ) -> None:
        """Construct."""
        self.header = header
        self.body = body
        self.query = query

    def __repr__(self) -> str:
        """Repr."""
        return f"""
        HttpRequest (header={self.header}, body={self.body},
        query={self.query})"""


class HttpResponse:
    """Class to http_response representation."""

    def __init__(self, status_code: int, body: any) -> None:
        """Construct."""
        self.body = body
        self.status_code = status_code

    def __repr__(self) -> str:
        """Repr."""
        return f"""HttpRequest (status_code={self.status_code},
        body={self.body})"""
