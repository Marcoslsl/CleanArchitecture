from src.infra.configs import DBConnectionHandler
from src.infra.entities import Users as UsersModel
from src.domain.models import Users


class UserRepository:
    """Class to manage User Repository."""

    @classmethod
    def insert_user(cls, name: str, password: str):
        """Insert data in user entity.

        Parameters
        ----------
        name: str
            Person name
        password: str
            User password
        return: namedtuple, None
            tuple with new user inserted
        """
        with DBConnectionHandler() as db_connection:
            try:
                new_user = UsersModel(name=name, password=password)
                db_connection.session.add(new_user)
                db_connection.session.commit()
                return Users(
                    id=new_user.id,
                    name=new_user.name,
                    password=new_user.password,
                )
            except Exception as e:
                db_connection.session.rollback()
                raise e
            finally:
                db_connection.session.close()

        return None
