from typing import List
from src.domain.models import Pets
from src.infra.configs import DBConnectionHandler
from src.infra.entities import Pets as PetsModel
from src.data.interfaces import PetRepositoryInterface


class PetsRepository(PetRepositoryInterface):
    """Class to manage Pet Repository."""

    @classmethod
    def insert_pet(
        cls, name: str, specie: str, age: int, user_id: int
    ) -> Pets:
        """Insert data in Pet entity.

        Parameters
        ----------
        name: str
            name of the pet
        specie: str
            enum with species acepted
        age: int
            specie age
        user_id: int
            id of the owner (FK)
        return: Pets
            Tuple with new pet inserted
        """
        with DBConnectionHandler() as db_conn:
            try:
                new_pet = PetsModel(
                    name=name, specie=specie, age=age, user_id=user_id
                )
                db_conn.session.add(new_pet)
                db_conn.session.commit()

                return Pets(
                    id=new_pet.id,
                    name=new_pet.name,
                    specie=new_pet.specie,
                    age=new_pet.age,
                    user_id=new_pet.user_id,
                )

            except Exception as e:
                db_conn.session.rollback()
                raise e
            finally:
                db_conn.session.close()

        return None

    @classmethod
    def select_pet(cls, pet_id: int = None, user_id: int = None) -> List[Pets]:
        """Select data in PetsENtity.

        Parameters
        ----------
        pet_id: int
            id of the pet registry
        user_id: int
            if of the owner
        return: List[Pets]
            List with peys selected
        """
        try:
            query_data = None
            if pet_id and not user_id:
                with DBConnectionHandler() as db_conn:
                    data = (
                        db_conn.session.query(PetsModel)
                        .filter_by(id=pet_id)
                        .one()
                    )
                    query_data = [data]
            elif not pet_id and user_id:
                with DBConnectionHandler() as db_conn:
                    data = (
                        db_conn.session.query(PetsModel)
                        .filter_by(user_id=user_id)
                        .all()
                    )
                    query_data = data
            elif pet_id and user_id:
                with DBConnectionHandler() as db_conn:
                    data = (
                        db_conn.session.query(PetsModel)
                        .filter_by(id=pet_id, user_id=user_id)
                        .one()
                    )
                    query_data = [data]

            return query_data
        except Exception as e:
            db_conn.session.rollback()
        finally:
            db_conn.session.close()

        return None
