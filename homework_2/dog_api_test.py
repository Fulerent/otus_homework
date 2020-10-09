import pytest
import cerberus


def test_status(url_api_dog):
    r = url_api_dog.get("breeds/list/all")
    r_status = r.json()['status']
    assert r_status == 'success'


@pytest.mark.parametrize("test_input", [1, 5, 13, 49])
def test_img_count(test_input, url_api_dog):
    r = url_api_dog.get(f"breeds/image/random/{test_input}")
    count_object = len(r.json()['message'])
    assert test_input == count_object


def test_breed_australian(url_api_dog):
    r = url_api_dog.get("breed/australian/list")
    dog = r.json()['message']
    assert dog == ['shepherd']


@pytest.mark.parametrize("test_input", ['hound', 'mountain', 'setter', 'spaniel'])
def test_list_breed(test_input, schema_dog_json, url_api_dog):
    r = url_api_dog.get(f"breed/{test_input}/list")
    v = cerberus.Validator()
    assert v.validate(r.json(), schema_dog_json)


def test_img_random(url_api_dog):
    r = url_api_dog.get("breed/beagle/images/random")
    beagle_dog = r.json()['status']
    assert beagle_dog == 'success'
