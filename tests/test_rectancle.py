import pytest

import source.shapes as shapes

@pytest.fixture
def my_rectangle():
    return shapes.Rectangle(10, 20)

@pytest.fixture
def weird_rectangle():
    return shapes.Rectangle(5, 6)

def test_area(my_rectangle):
    # my_rectangle = shapes.Rectangle(10, 20)
    assert my_rectangle.area() == 10 * 20

def test_perimeter(my_rectangle):
    # my_rectangle = shapes.Rectangle(10, 20)
    assert my_rectangle.perimeter() == 2 * (10 + 20)

def test_not_equal(my_rectangle, weird_rectangle):
    assert my_rectangle != weird_rectangle