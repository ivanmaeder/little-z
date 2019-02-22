from pizza import pizzeria_area

def test_size_0():
    assert [(0, 0)] == pizzeria_area(0, 0, 0)

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
