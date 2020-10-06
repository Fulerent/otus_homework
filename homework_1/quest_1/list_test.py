import pytest
def test_list_one():
    list_to_test = []
    assert list_to_test == []


def test_list_two():
    list_to_test = []
    assert len(list_to_test) == 0


def test_list_three():
    list_to_test = [1, 2, 3]
    assert len(list_to_test) == 3


def test_list_four():
    list_to_test = ['one', 'two', 'three']
    assert list_to_test[1] == 'two'


@pytest.mark.parametrize("test_input", ['abc', 'bac', 'bca'])
def test_list_five(test_input):
    element = set(test_input)
    assert len(element) == 3


