import pytest

def test_set_one():
    set_to_test = {}
    assert set_to_test == {}


def test_set_two():
    set_to_test1 = {1, 3, 5, 7, 9}
    set_to_test2 = {2, 3, 6, 8}
    assert set_to_test1 & set_to_test2 == {3}


def test_set_three():
    set_to_test = {"java", "python", "js"}
    assert 'python' in set_to_test


def test_set_four():
    set_to_test1 = {1, 3, 5, 7, 9}
    set_to_test2 = {2, 3, 5, 7}
    assert set_to_test1 - set_to_test2 == {1, 9}


@pytest.mark.parametrize("test_input", {3, 8, 11.12, 26, 0.5})
def test_set_five(test_input):
    assert test_input > 0
