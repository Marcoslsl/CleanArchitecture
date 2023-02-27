from faker import Faker
from src.data.find_user import FindUser
from src.infra.tests import UserRepositorySpy

faker = Faker()


def test_by_id():
    user_repo = UserRepositorySpy()
    find_user = FindUser(user_repo)

    attributes = {"id": faker.random_number(digits=2)}

    response = find_user.by_id(user_id=attributes["id"])

    assert user_repo.select_user_params["user_id"] == attributes["id"]

    assert response["Success"] is True
    assert response["Data"]


# TO DO
# OUTROS TESTES
