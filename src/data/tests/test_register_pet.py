from faker import Faker
from src.data.register_pet import RegisterPet
from src.infra.tests import PetRepositorySpy, UserRepositorySpy
from src.data.spy import FindUserSpy

faker = Faker()


def test_register():
    pet_repo = PetRepositorySpy()
    find_user = FindUserSpy(UserRepositorySpy())
    register_pet = RegisterPet(pet_repo, find_user)

    attributes = {
        "name": faker.name(),
        "specie": faker.name(),
        "age": faker.random_number(),
        "user_information": {
            "user_id": faker.random_number(),
            "user_name": faker.name(),
        },
    }

    response = register_pet.register(
        name=attributes["name"],
        specie=attributes["specie"],
        age=attributes["age"],
        user_information=attributes["user_information"],
    )

    assert pet_repo.insert_pets_params["name"] == attributes["name"]
    assert pet_repo.insert_pets_params["age"] == attributes["age"]
    assert pet_repo.insert_pets_params["specie"] == attributes["specie"]

    assert (
        find_user.by_id_and_name_param["user_id"]
        == attributes["user_information"]["user_id"]
    )
    assert (
        find_user.by_id_and_name_param["name"]
        == attributes["user_information"]["user_name"]
    )

    assert response["Success"] is True
    assert response["Data"]
