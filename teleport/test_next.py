import math

from main import next

def test_earth_when_all_unvisited():
    unvisited_nodes = ["A", "B", "C"]

    priority_queue = {
        "A" : 0,
        "B" : math.inf,
        "C" : math.inf,
    }

    assert "A" == next(unvisited_nodes, priority_queue)

def test_next_unvisited_is_not_best():
    unvisited_nodes = ["B", "C"]

    priority_queue = {
        "A" : 0,
        "B" : 3,
        "C" : 1,
    }

    assert "C" == next(unvisited_nodes, priority_queue)
