from faker import Faker
from src.data.spy import RegisterPetSpy
from src.infra.tests import PetRepositorySpy
from src.presenters.controllers import RegisterPetController
from src.presenters.helpers import HttpRequest

faker = Faker()


def test_route():
    register_pet_use_case = RegisterPetSpy(PetRepositorySpy(), None)
    register_pet_route = RegisterPetController(register_pet_use_case)

    attributer = {
        "name": faker.word(),
        "specie": "Dog",
        "age": faker.random_number(),
        "user_information": {
            "user_id": faker.random_number(),
            "user_name": faker.word(),
        },
    }

    response = register_pet_route.route(HttpRequest(body=attributer))

    assert register_pet_use_case.register_param["name"] == attributer["name"]
    assert (
        register_pet_use_case.register_param["specie"] == attributer["specie"]
    )
    assert register_pet_use_case.register_param["age"] == attributer["age"]
    assert (
        register_pet_use_case.register_param["user_information"]
        == attributer["user_information"]
    )

    assert response.status_code == 200
    assert "error" not in response.body
