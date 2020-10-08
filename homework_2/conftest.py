import pytest
import requests


class ApiClient:
    def __init__(self, base_address):
        self.base_address = base_address

    def get(self, path="/", params=None):
        url = self.base_address + path
        return requests.get(url=url, params=params)


@pytest.fixture(scope="session")
def url_api_dog(request):
    return ApiClient(base_address="https://dog.ceo/api/")

@pytest.fixture(scope="session")
def url_api_dog(request):
    return ApiClient(base_address="https://dog.ceo/api/")

@pytest.fixture()
def schema_dog_json():
    schema = {
        "message": {"type": "array"},
        "status": {"type": "string"}
    }
    return schema
