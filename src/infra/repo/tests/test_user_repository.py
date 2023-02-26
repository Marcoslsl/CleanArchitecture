from faker import Faker
from src.infra.repo import UserRepository
from src.infra.configs import DBConnectionHandler
from sqlalchemy import text

db_conn = DBConnectionHandler()
user_repo = UserRepository()

faker = Faker()
name = faker.name()
pswd = faker.word()


def test_insert_user():
    engine = db_conn.get_engine()

    new_user = user_repo.insert_user(name=name, password=pswd)

    with engine.connect() as conn:
        query_select = f"""SELECT * FROM users WHERE id={new_user.id}"""
        query_user = conn.execute(text(query_select)).fetchone()
        query_delete = f"""DELETE FROM users WHERE id={new_user.id}"""
        conn.execute(text(query_delete))
        conn.commit()

    assert new_user.id == query_user.id
    assert new_user.name == query_user.name
    assert new_user.password == query_user.password
