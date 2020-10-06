import pytest


def test_string_one():
    dict_to_test = ' '
    assert dict_to_test == ' '


def test_string_two():
    dict_to_test = 'abc'
    assert dict_to_test == 'abc'


def test_string_three():
    dict_to_test = 'много букв'
    assert len(dict_to_test) == 10


def test_string_four():
    dict_to_test = 'много букв'
    assert len(dict_to_test) == 10


@pytest.mark.parametrize("test_input", {'первая строка', 'вторая строка', 'и еще одна'})
def test_dict_five(test_input):
    assert 6 < len(test_input) < 15



