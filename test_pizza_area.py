from pizza import pizzeria_area

def test_size_0():
    expected = [(0, 0)]
    
    assert expected == pizzeria_area(0, 0, 0)

def test_size_1():
    expected = [         (-1, 0),
                (0, -1), ( 0, 0), (0, 1),
                         ( 1, 0)        ]

    assert expected == pizzeria_area(0, 0, 1)

def test_size_2():
    expected = [                   (-2, 0), 
                         (-1, -1), (-1, 0), (-1, 1),
                (0, -2), ( 0, -1), ( 0, 0), ( 0, 1), (0, 2),
                         ( 1, -1), ( 1, 0), ( 1, 1),
                                   ( 2, 0)                  ]

    assert expected == pizzeria_area(0, 0, 2)

def test_size_3():
    expected = [                             (-3, 0),
                                   (-2, -1), (-2, 0), (-2, 1),
                         (-1, -2), (-1, -1), (-1, 0), (-1, 1), (-1, 2),
                (0, -3), ( 0, -2), ( 0, -1), ( 0, 0), ( 0, 1), ( 0, 2), (0, 3),
                         ( 1, -2), ( 1, -1), ( 1, 0), ( 1, 1), ( 1, 2),
                                   ( 2, -1), ( 2, 0), ( 2, 1),
                                             ( 3, 0)                           ]

    assert expected == pizzeria_area(0, 0, 3)

def test_size_0_different_location():
    expected = [(2, 7)]

    assert expected == pizzeria_area(2, 7, 0)

def test_size_2_different_location():
    expected = [                (1, 9),
                        (2, 8), (2, 9), (2, 10),
                (3, 7), (3, 8), (3, 9), (3, 10), (3, 11),
                        (4, 8), (4, 9), (4, 10),
                                (5, 9)                   ]

    assert expected == pizzeria_area(3, 9, 2)
