from src.domain.models import Pets
from src.infra.configs import DBConnectionHandler
from src.infra.entities import Pets as PetsModel


class PetsRepository:
    """Class to manage Pet Repository."""

    @classmethod
    def isert_pet(cls, name: str, specie: str, age: int, user_id: int) -> Pets:
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
