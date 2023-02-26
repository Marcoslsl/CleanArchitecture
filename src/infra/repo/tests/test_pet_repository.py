from faker import Faker
from src.infra.repo import PetsRepository
from src.infra.configs import DBConnectionHandler
from sqlalchemy import text
from src.infra.entities import Pets as PetsModel


db_conn = DBConnectionHandler()
pets_repo = PetsRepository()

faker = Faker()

name = faker.name()
specie = "fish"
age = faker.random_number(digits=1)
user_id = faker.random_number()


def test_insert_pet():
    new_pet = pets_repo.isert_pet(
        name=name, specie=specie, age=age, user_id=user_id
    )

    engine = db_conn.get_engine()
    with engine.connect() as conn:
        query_select = f"""SELECT * FROM pets WHERE id={new_pet.id}"""
        query_pets = conn.execute(text(query_select)).fetchone()
        query_delete = f"""DELETE FROM pets WHERE id={new_pet.id}"""
        conn.execute(text(query_delete))
        conn.commit()

    assert new_pet.id == query_pets.id
    assert new_pet.name == query_pets.name
    assert new_pet.age == query_pets.age
    assert new_pet.user_id == query_pets.user_id
    assert new_pet.specie.value == query_pets.specie
