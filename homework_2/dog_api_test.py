import pytest
from jsonschema import validate


def test_status(url_api_dog):
    r = url_api_dog.get("breeds/list/all")
    r_status = r.json()['status']
    assert r_status == 'success'


@pytest.mark.parametrize("test_input", [1, 5, 13, 49])
def test_img_count(test_input, url_api_dog):
    random_count = test_input
    r = url_api_dog.get(f"breeds/image/random/{random_count}")
    count_object = len(r.json()['message'])
    assert test_input == count_object


def test_breed_australian(url_api_dog):
    r = url_api_dog.get("breed/australian/list")
    dog = r.json()['message']
    assert dog == ['shepherd']


@pytest.mark.parametrize("test_input", ['hound', 'mountain', 'setter', 'spaniel'])
def test_list_breed(test_input, schema_dog_json, url_api_dog):
    r = url_api_dog.get("breed/{test_input}/list")
    validate(instance=r.json(), schema=schema_dog_json)


def test_img_random(url_api_dog):
    r = url_api_dog.get("breed/beagle/images/random")
    beagle_dog = r.json()['status']
    assert beagle_dog == 'success'
