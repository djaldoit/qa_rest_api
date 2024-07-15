import pytest

DOMAIN_URL = "https://reqres.in"
USERS_API = "/api/users"
RESOURCES_API = "/api/unknown"
LOGIN_API = "/api/register"


@pytest.fixture()
def base_endpoint():
    base_endpoint = DOMAIN_URL + USERS_API
    resources_endpoint = DOMAIN_URL + RESOURCES_API
    login_endpoint = DOMAIN_URL + LOGIN_API
    return base_endpoint, resources_endpoint, login_endpoint
