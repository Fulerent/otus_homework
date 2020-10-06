import pytest


def test_dict_one():
    dict_to_test = {}
    assert dict_to_test == {}


def test_dict_two():
    dict_to_test = {'one': 1, 'two': 2, "three": 3}
    assert dict_to_test["three"] == 3


def test_dict_three():
    dict_to_test = {'one': 1, 'two': 2, "three": 3}
    assert dict_to_test.get('family') is None


def test_dict_four():
    dict_to_test = {'one': 1, 'two': 2, "three": 3}
    assert dict_to_test.get('four') is None


@pytest.mark.parametrize("test_input", {'one': 1, 'two': 2, "three": 3})
def test_dict_five(test_input):
    assert '4' not in test_input


