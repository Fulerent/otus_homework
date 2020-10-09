import pytest
import cerberus


def test_id(url_api_breweries):
    r = url_api_breweries.get("777")
    response = r.json()
    assert response['id'] == 777


@pytest.mark.parametrize("test_input", ['dog', 'home', 'green', 'evil'])
def test_list_breweries(url_api_breweries, test_input):
    r = url_api_breweries.get(f"autocomplete?query={test_input}")
    response = r.json()
    assert len(response) >= 1


@pytest.mark.parametrize("test_input", range(1, 3))
def test_structure_response(test_input, url_api_breweries, schema_breweries_json):
    r = url_api_breweries.get(f"{test_input}")
    v = cerberus.Validator()
    assert v.validate(r.json(), schema_breweries_json)


@pytest.mark.parametrize("test_input", [1, 10, 25, 50])
def test_breweries_per_page(test_input, url_api_breweries):
    r = url_api_breweries.get(f"?per_page={test_input}")
    assert len(r.json()) == test_input


def test_brewery_type(url_api_breweries):
    r = url_api_breweries.get("?by_type=micro")
    response = r.json()
    for i in response:
        assert i['brewery_type'] == 'micro'


