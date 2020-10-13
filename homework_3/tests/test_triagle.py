import pytest
from homework_3.figure import *


@pytest.mark.parametrize('input_abc', [(2, 5, 3), (3, 7, 5), (7, 4, 10)])
def test_name(input_abc):
    figure = Triangle(input_abc[0], input_abc[1], input_abc[2])
    assert figure.name() == "Triangle"


@pytest.mark.parametrize('input_abc', [(2, 5, 3, '10'), (3, 7, 5, '10'), (7, 4, 10, '10')])
def test_area(input_abc):
    figure = Triangle(input_abc[0], input_abc[1], input_abc[2])
    assert figure.area() == int(input_abc[3])


@pytest.mark.parametrize('input_abc', [(2, 5, 3), (3, 7, 5), (7, 4, 10)])
def test_angles(input_abc):
    figure = Triangle(input_abc[0], input_abc[1], input_abc[2])
    assert figure.angles() == 4


@pytest.mark.parametrize('input_abc', [(2, 5, "14"), (3, 7, "20"), (5, 3, "16")])
def test_perimeter(input_ab):
    figure = Triangle(input_ab[0], input_ab[1])
    assert figure.perimeter() == int(input_ab[2])

