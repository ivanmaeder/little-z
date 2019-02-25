from main import Coordinate, distance

def test_distance1():
    coordinate1 = Coordinate(2, 0, 1)
    coordinate2 = Coordinate(-5, -6, -5)

    assert 11 == distance(coordinate1, coordinate2)

def test_distance2():
    coordinate1 = Coordinate(2, 1, 2)
    coordinate2 = Coordinate(1, 1, 0)

    assert 2.24 == distance(coordinate1, coordinate2)
