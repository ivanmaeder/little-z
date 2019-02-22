from pizza import pizzeria_area

#def test_size_0():
#    assert [(1, 1)] == pizzeria_area(1, 1, 0)

#def test_size_0_different_location():
#    assert [(2, 7)] == pizzeria_area(2, 7, 0)

def test_size_1():
    assert [(-1, 0), (0, -1), (0, 0), (0, 1), (1, 0)] == pizzeria_area(0, 0, 1)
    #assert [(2, 3), (1, 2), (2, 2), (3, 2), (2, 1)] == pizzeria_area(2, 2, 1)

def test_size_2():
    assert [(-2, 0), (-1, -1), (-1, 0), (-1, 1), (0, -2), (0, -1), (0, 0), (0, 1), (0, 2), (1, -1), (1, 0), (1, 1), (2, 0)] == pizzeria_area(0, 0, 2)
#    assert [(3, 5), (2, 4), (3, 4), (4, 4), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (2, 2), (3, 2), (4, 2), (3, 1)] == pizzeria_area(3, 3, 2)

def test_size_3():
    assert [(-3, 0), (-2, -1), (-2, 0), (-2, 1), (-1, -2), (-1, -1), (-1, 0), (-1, 1), (-1, 2), (0, -3), (0, -2), (0, -1), (0, 0), (0, 1), (0, 2), (0, 3), (1, -2), (1, -1), (1, 0), (1, 1), (1, 2), (2, -1), (2, 0), (2, 1), (3, 0)] == pizzeria_area(0, 0, 3)
