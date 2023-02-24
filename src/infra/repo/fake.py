from src.infra.configs import DBConnectionHandler
from src.infra.entities import Users


class FakerRepo:
    """A simple repository."""

    @classmethod
    def insert_user(cls):
        """Something."""
        with DBConnectionHandler() as db_connection:
            try:
                new_user = Users(name="marcos", password="1234")
                db_connection.session.add(new_user)
                db_connection.session.commit()
            except Exception as e:
                db_connection.session.rollback()
                raise e
            finally:
                db_connection.session.close()
