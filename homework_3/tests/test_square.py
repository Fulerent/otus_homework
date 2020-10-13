import pytest
from homework_3.figure import *


@pytest.mark.parametrize('input_a', [5, 10, 15])
def test_name(input_a):
    figure = Square(input_a)
    assert figure.name() == "Square"


@pytest.mark.parametrize('input_a', [(5, '25'), (3, '9'), (7, '49')])
def test_area(input_a):
    figure = Square(input_a[0])
    assert figure.area() == int(input_a[1])


@pytest.mark.parametrize('input_a', [5, 10, 15])
def test_angles(input_a):
    figure = Square(input_a)
    assert figure.angles() == 4


@pytest.mark.parametrize('input_a', [(4, '16'), (3, '12'), (7, '28')])
def test_perimeter(input_a):
    figure = Square(input_a[0])
    assert figure.perimeter() == int(input_a[1])