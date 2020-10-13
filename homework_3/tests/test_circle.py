import pytest
from homework_3.figure import *


@pytest.mark.parametrize('input_radius', [0.5, 1.3, 2.7])
def test_name(input_radius):
    figure = Circle(input_radius)
    assert figure.name() == "Circle"


@pytest.mark.parametrize('input_radius', [(5, "78.54"), (3, "28.27"), (7, "153.94")])
def test_area(input_radius):
    figure = Circle(input_radius[0])
    assert figure.area() == float(input_radius[1])


@pytest.mark.parametrize('input_radius', [5, 10, 15])
def test_angles(input_radius):
    figure = Circle(input_radius)
    assert figure.angles() == 0


@pytest.mark.parametrize('input_radius', [(4, "25.13"), (3, "18.85"), (7, "43.98")])
def test_perimeter(input_radius):
    figure = Circle(input_radius[0])
    assert figure.perimeter() == float(input_radius[1])





