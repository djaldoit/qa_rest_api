import pytest
import requests
from resources.data import complete_creds, incomplete_creds


@pytest.mark.positive
def test_register_successful(base_endpoint):
    response = requests.post(url=base_endpoint[2], data=complete_creds)

    assert response.status_code == 200
    assert 'id' in response.json() and 'token' in response.json()


@pytest.mark.negative
def test_register_unsuccessful(base_endpoint):
    response = requests.post(url=base_endpoint[2], data=incomplete_creds)

    assert response.status_code == 400
    assert 'error' in response.json()
    assert response.json()["error"] == "Missing password"
