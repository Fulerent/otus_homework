import pytest
import requests


@pytest.fixture(scope="session")
def api_client(request):
    url = request.config.getoption("--url")
    status_code = request.config.getoption("--status_code")
    return requests.get(url), int(status_code)


#pytest get_status_test.py --url=https://ya.ru/sfhfhfhfhfhfhfhfh --status_code=404

def test_get_status_code(api_client):
    r, status_code = api_client
    assert r.status_code == status_code
