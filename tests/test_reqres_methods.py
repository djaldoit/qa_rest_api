import pytest
import requests
from resources.data import data_for_post, data_for_update, existing_user_id, not_existing_user_id


@pytest.mark.positive
def test_get_user(base_endpoint):
    response = requests.get(url=f"{base_endpoint[0]}/{existing_user_id}")

    assert response.status_code == 200
    assert response.json()['data']['id'] == existing_user_id


@pytest.mark.negative
def test_get_not_existing_user(base_endpoint):
    response = requests.get(url=f"{base_endpoint[0]}/{not_existing_user_id}")

    assert response.status_code == 404
    assert response.json() == {}


def test_create_user(base_endpoint):
    response = requests.post(url=base_endpoint[0], json=data_for_post)

    assert response.status_code == 201
    assert response.json()["name"] == data_for_post["name"]
    assert response.json()["job"] == data_for_post["job"]


def test_update_user(base_endpoint):
    response = requests.put(url=f"{base_endpoint[0]}/2", json=data_for_update)

    assert response.status_code == 200
    assert response.json()["name"] == data_for_update["name"]
    assert response.json()["job"] == data_for_update["job"]


def test_delete_user(base_endpoint):
    response = requests.delete(url=f"{base_endpoint[0]}/2")

    assert response.status_code == 204
