import pytest
import source.shapes as shapes

@pytest.mark.parametrize("side_length, expected_area", [(5, 25), (4, 16), (9, 81)])
def test_many_square_areas(side_length, expected_area):
    assert shapes.Square(side_length).area() == expected_area

@pytest.mark.parametrize("side_length, expected_perimeter", [(1, 4), (2, 8), (10, 40)])
def test_many_square_perimeters(side_length, expected_perimeter):
    assert shapes.Square(side_length).perimeter() == expected_perimeter