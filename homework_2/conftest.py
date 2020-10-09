import pytest
import requests


class ApiClient:
    def __init__(self, base_address):
        self.base_address = base_address

    def get(self, path="/", params=None):
        url = self.base_address + path
        return requests.get(url=url, params=params)

    def post(self, path="/", json=None):
        url = self.base_address + path
        return requests.post(url=url, json=json)


@pytest.fixture(scope="session")
def url_api_dog(request):
    return ApiClient(base_address="https://dog.ceo/api/")


@pytest.fixture(scope="session")
def url_api_breweries(request):
    return ApiClient(base_address="https://api.openbrewerydb.org/breweries/")


@pytest.fixture(scope="session")
def url_api_jsonplaceholder(request):
    return ApiClient(base_address="https://jsonplaceholder.typicode.com/")


@pytest.fixture()
def schema_dog_json():
    schema = {
        "message": {"type": "list"},
        "status": {"type": "string"}
    }
    return schema


@pytest.fixture()
def schema_breweries_json():
    schema = {
        "id": {"type": "number"},
        "name": {"type": "string"},
        "brewery_type": {"type": "string"},
        "street": {"type": "string"},
        "city": {"type": "string"},
        "state": {"type": "string"},
        "postal_code": {"type": "string"},
        "country": {"type": "string"},
        "longitude": {"type": "string"},
        "latitude": {"type": "string"},
        "phone": {"type": "string"},
        "website_url": {"type": "string"},
        "updated_at": {"type": "string"}
        }
    return schema


@pytest.fixture()
def schema_jsonplaceholder_comment_json():
    schema = {
        "postId": {"type": "number"},
        "id": {"type": "number"},
        "name": {"type": "string"},
        "email": {"type": "string"},
        "body": {"type": "string"},
        }
    return schema


@pytest.fixture()
def count_element_response():
    return {'posts': 100, 'comments': 500, 'albums': 100, 'photos': 5000, 'todos': 200, 'users': 10}


@pytest.fixture()
def jsonplaceholder_post():
    return '"title": "Test43s","body": "qa_otus_2020","userId": 43242343}'


#задание4 url

def pytest_addoption(parser):
    parser.addoption("--url",
                     action="store",
                     default="https://ya.ru/",
                     help="This is request url.")
    parser.addoption("--status_code",
                     action="store",
                     default=200,
                     help="Status code.")