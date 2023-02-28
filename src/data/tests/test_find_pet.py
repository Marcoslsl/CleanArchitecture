from faker import Faker
from src.data.find_pet import FindPet
from src.infra.tests import PetRepositorySpy

faker = Faker()


def test_by_id():
    pet_repo = PetRepositorySpy()
    find_pet = FindPet(pet_repo)

    attributes = {"id": faker.random_number(digits=2)}

    response = find_pet.by_id(user_id=attributes["id"])

    assert pet_repo.select_pets_params["user_id"] == attributes["id"]

    assert response["Success"] is True
    assert response["Data"]


def test_by_pet_id():
    pet_repo = PetRepositorySpy()
    find_pet = FindPet(pet_repo)

    attributes = {"pet_id": faker.random_number(digits=2)}

    response = find_pet.by_pet_id(pet_id=attributes["pet_id"])

    assert pet_repo.select_pets_params["pet_id"] == attributes["pet_id"]

    assert response["Success"] is True
    assert response["Data"]


def test_by_id_and_pet_id():
    pet_repo = PetRepositorySpy()
    find_pet = FindPet(pet_repo)

    attributes = {
        "id": faker.random_number(digits=2),
        "pet_id": faker.random_number(digits=2),
    }

    response = find_pet.by_id_and_pet_id(
        user_id=attributes["id"], pet_id=attributes["pet_id"]
    )

    assert pet_repo.select_pets_params["pet_id"] == attributes["pet_id"]

    assert response["Success"] is True
    assert response["Data"]
