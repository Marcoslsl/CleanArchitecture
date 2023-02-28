from faker import Faker
from src.presenters.controllers import FindUserController
from src.data.spy import FindUserSpy
from src.infra.tests import UserRepositorySpy
from src.presenters.helpers import HttpRequest

faker = Faker()


def test_handler():
    find_user_use_case = FindUserSpy(UserRepositorySpy())
    find_user_controller = FindUserController(find_user_use_case)

    http_request = HttpRequest(
        query={"user_id": faker.random_number(), "user_name": faker.word()}
    )
    response = find_user_controller.route(http_request)

    assert (
        find_user_use_case.by_id_and_name_param["user_id"]
        == http_request.query["user_id"]
    )
    assert (
        find_user_use_case.by_id_and_name_param["name"]
        == http_request.query["user_name"]
    )

    assert response.status_code == 200
    assert response.body
