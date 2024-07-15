import requests
import json
from jsonschema import validate
from resources import resource
from resources.data import data_for_post
from resources.schemas.create_user import CreateUser
from resources.schemas.get_single_user import GetUser


def test_validate_get_list_resources_schema(base_endpoint):
    response = requests.get(url=base_endpoint[1])

    get_list_schema = json.load(open(resource.path('get_list_resources.json')))
    validate(response.json(), get_list_schema)


def test_validate_get_single_resource_schema(base_endpoint):
    response = requests.get(url=f"{base_endpoint[1]}/2")

    get_resource_schema = json.load(open(resource.path('get_single_resource.json')))
    validate(response.json(), get_resource_schema)


def test_validate_get_single_user_schema(base_endpoint):
    response = requests.get(url=f"{base_endpoint[0]}/2")

    validate(response.json(), GetUser)


def test_validate_create_user_schema(base_endpoint):
    response = requests.post(url=base_endpoint[0], data=data_for_post)

    validate(response.json(), CreateUser)
