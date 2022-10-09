from Coordinate import Coordinate
from Quadrant import Quadrant

def test_should_get_first_quadrant_coordinate():
    # Arrange / Setup
    coord_x = 2
    coord_y = 2
    coordinates = Coordinate(coord_x, coord_y)
    quadrant = Quadrant(coordinates)

    # Act / Action
    result = quadrant.get_quadrant_coordinate()

    # Assert
    assert result == "First"


def test_should_get_second_quadrant_coordinate():
    # Arrange / Setup
    coord_x = -7
    coord_y = 1
    coordinates = Coordinate(coord_x, coord_y)
    quadrant = Quadrant(coordinates)

    # Act / Action
    result = quadrant.get_quadrant_coordinate()

    # Assert
    assert result == "Second"

def test_should_get_third_quadrant_coordinate():
    # Arrange / Setup
    coord_x = -8
    coord_y = -1
    coordinates = Coordinate(coord_x, coord_y)
    quadrant = Quadrant(coordinates)

    # Act / Action
    result = quadrant.get_quadrant_coordinate()

    # Assert
    assert result == "Third"

def test_should_get_fourth_quadrant_coordinate():
    # Arrange / Setup
    coord_x = 3
    coord_y = -2
    coordinates = Coordinate(coord_x, coord_y)
    quadrant = Quadrant(coordinates)

    # Act / Action
    result = quadrant.get_quadrant_coordinate()

    # Assert
    assert result == "Fourth"


def test_should_get_empty_string_quadrant_coordinate():
    # Arrange / Setup
    coord_x = 0
    coord_y = 2
    coordinates = Coordinate(coord_x, coord_y)
    quadrant = Quadrant(coordinates)

    # Act / Action
    result = quadrant.get_quadrant_coordinate()

    # Assert
    assert result == ""
