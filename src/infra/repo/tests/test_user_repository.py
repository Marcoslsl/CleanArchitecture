from faker import Faker
from src.infra.repo import UserRepository
from src.infra.configs import DBConnectionHandler
from sqlalchemy import text
from src.infra.entities import Users as UsersModel

db_conn = DBConnectionHandler()
user_repo = UserRepository()

faker = Faker()
user_id = faker.random_number(digits=5)
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


def test_select_user():
    data = UsersModel(id=user_id, name=name, password=pswd)

    engine = db_conn.get_engine()
    with engine.connect() as conn:
        conn.execute(
            text(
                f"""INSERT INTO users (id, name, password)
            VALUES ({user_id}, '{name}', '{pswd}')"""
            )
        )
        conn.commit()

    query_user1 = user_repo.select_user(user_id=user_id)
    query_user2 = user_repo.select_user(name=name)
    query_user3 = user_repo.select_user(user_id=user_id, name=name)

    assert data in query_user1
    assert data in query_user2
    assert data in query_user3

    with engine.connect() as conn:
        conn.execute(text(f"""DELETE FROM users WHERE id='{user_id}'"""))
        conn.commit()
