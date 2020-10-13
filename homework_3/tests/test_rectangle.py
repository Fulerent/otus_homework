import pytest
from homework_3.figure import *


@pytest.mark.parametrize('input_ab', [(2, 5), (3, 7), (5, 2)])
def test_name(input_ab):
    figure = Rectangle(input_ab[0], input_ab[1])
    assert figure.name() == "Rectangle"


@pytest.mark.parametrize('input_ab', [(2, 5, "10"), (3, 7, "21"), (5, 3, "15")])
def test_area(input_ab):
    figure = Rectangle(input_ab[0], input_ab[1])
    assert figure.area() == int(input_ab[2])


@pytest.mark.parametrize('input_ab', [(2, 5), (3, 7), (5, 2)])
def test_angles(input_ab):
    figure = Rectangle(input_ab[0], input_ab[1])
    assert figure.angles() == 4


@pytest.mark.parametrize('input_ab', [(2, 5, "14"), (3, 7, "20"), (5, 3, "16")])
def test_perimeter(input_ab):
    figure = Rectangle(input_ab[0], input_ab[1])
    assert figure.perimeter() == int(input_ab[2])

