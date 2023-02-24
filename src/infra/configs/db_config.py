from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBConnectionHandler:
    """Sqlaclhemy database connection."""

    def __init__(self) -> None:
        """Construct."""
        self.__connection_string = "sqlite:///storage.db"
        self.session = None

    def get_engine(self):
        """Return connection engine."""
        engine = create_engine(self.__connection_string)
        return engine

    def __enter__(self):
        """Enter."""
        engine = create_engine(self.__connection_string)
        session_maker = sessionmaker()
        self.session = session_maker(bind=engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Exit."""
        self.session.close()
