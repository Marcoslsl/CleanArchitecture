from typing import List
from src.infra.configs import DBConnectionHandler
from src.infra.entities import Users as UsersModel
from src.domain.models import Users
from src.data.interfaces import UserRepositoryInterface


class UserRepository(UserRepositoryInterface):
    """Class to manage User Repository."""

    @classmethod
    def insert_user(cls, name: str, password: str) -> Users:
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

    @classmethod
    def select_user(cls, user_id: int = None, name: str = None) -> List[Users]:
        """Select data in user entity.

        Parameters
        ----------
        user_id: int, default=None
            Id of the register
        name: str, default=None
            User name
        return: list
            List with users selected
        """
        try:
            query = None

            if user_id and not name:
                with DBConnectionHandler() as db_conn:
                    data = (
                        db_conn.session.query(UsersModel)
                        .filter_by(id=user_id)
                        .one()
                    )
                    query = [data]

            elif not user_id and name:
                with DBConnectionHandler() as db_conn:
                    data = (
                        db_conn.session.query(UsersModel)
                        .filter_by(name=name)
                        .one()
                    )
                    query = [data]

            elif user_id and name:
                with DBConnectionHandler() as db_conn:
                    data = (
                        db_conn.session.query(UsersModel)
                        .filter_by(id=user_id, name=name)
                        .one()
                    )
                    query = [data]

            return query

        except Exception as e:
            db_conn.session.rollback()
            raise e
        finally:
            db_conn.session.close()
