import math
import networkx as nx

from main import find_optimal_path

def test_zero_stations():
    g = nx.Graph()
    g.add_node("A")

    g.add_edge("B", "A", weight=1)

    assert 1 == find_optimal_path(g, "A", "B")

def test_1_station_all_weights_equal():
    g = nx.Graph()
    g.add_node("A")

    g.add_edge("B", "A", weight=4)
    g.add_edge("C", "A", weight=4)

    g.add_edge("C", "B", weight=4)

    assert 4 == find_optimal_path(g, "A", "C")

def test_1_station_direct():
    g = nx.Graph()
    g.add_node("A")

    g.add_edge("B", "A", weight=5)
    g.add_edge("C", "A", weight=2)

    g.add_edge("C", "B", weight=5)

    assert 2 == find_optimal_path(g, "A", "C")

def test_1_station_indirect():
    g = nx.Graph()
    g.add_node("A")

    g.add_edge("B", "A", weight=3)
    g.add_edge("C", "A", weight=5)

    g.add_edge("C", "B", weight=3)

    assert 3 == find_optimal_path(g, "A", "C")

def test_2_stations_all_weights_equal():
    g = nx.Graph()
    g.add_node("A")

    g.add_edge("B", "A", weight=5)
    g.add_edge("C", "A", weight=5)
    g.add_edge("D", "A", weight=5)

    g.add_edge("C", "B", weight=5)
    g.add_edge("D", "B", weight=5)

    g.add_edge("C", "D", weight=5)

    assert 5 == find_optimal_path(g, "A", "D")

def test_2_stations_direct():
    g = nx.Graph()
    g.add_node("A")

    g.add_edge("B", "A", weight=9)
    g.add_edge("C", "A", weight=9)
    g.add_edge("D", "A", weight=5)

    g.add_edge("C", "B", weight=9)
    g.add_edge("D", "B", weight=9)

    g.add_edge("C", "D", weight=9)

    assert 5 == find_optimal_path(g, "A", "D")

def test_2_stations_backtrack():
    g = nx.Graph()
    g.add_node("A")

    g.add_edge("B", "A", weight=1)
    g.add_edge("C", "A", weight=5)
    g.add_edge("D", "A", weight=5)

    g.add_edge("C", "B", weight=5)
    g.add_edge("D", "B", weight=10)

    g.add_edge("C", "D", weight=10)

    assert 5 == find_optimal_path(g, "A", "D")

def test_3_stations_all_weights_equal():
    g = nx.Graph()
    g.add_node("A")

    g.add_edge("B", "A", weight=5)
    g.add_edge("C", "A", weight=5)
    g.add_edge("D", "A", weight=5)
    g.add_edge("E", "A", weight=5)

    g.add_edge("C", "B", weight=5)
    g.add_edge("D", "B", weight=5)
    g.add_edge("E", "B", weight=5)

    g.add_edge("D", "C", weight=5)
    g.add_edge("E", "C", weight=5)

    g.add_edge("E", "D", weight=5)

    assert 5 == find_optimal_path(g, "A", "E")

def test_3_stations_direct():
    g = nx.Graph()
    g.add_node("A")

    g.add_edge("B", "A", weight=5)
    g.add_edge("C", "A", weight=5)
    g.add_edge("D", "A", weight=5)
    g.add_edge("E", "A", weight=1)

    g.add_edge("C", "B", weight=5)
    g.add_edge("D", "B", weight=5)
    g.add_edge("E", "B", weight=5)

    g.add_edge("D", "C", weight=5)
    g.add_edge("E", "C", weight=5)

    g.add_edge("E", "D", weight=5)

    assert 1 == find_optimal_path(g, "A", "E")

def test_3_stations_multiple_hops():
    g = nx.Graph()
    g.add_node("A")

    g.add_edge("B", "A", weight=1)
    g.add_edge("C", "A", weight=5)
    g.add_edge("D", "A", weight=5)
    g.add_edge("E", "A", weight=5)

    g.add_edge("C", "B", weight=5)
    g.add_edge("D", "B", weight=1)
    g.add_edge("E", "B", weight=5)

    g.add_edge("D", "C", weight=5)
    g.add_edge("E", "C", weight=5)

    g.add_edge("E", "D", weight=1)

    assert 1 == find_optimal_path(g, "A", "E")

def test_4_stations_indirect():
    g = nx.Graph()
    g.add_node("A")

    g.add_edge("B", "A", weight=4)
    g.add_edge("C", "A", weight=4)
    g.add_edge("D", "A", weight=1)
    g.add_edge("E", "A", weight=4)
    g.add_edge("F", "A", weight=4)

    g.add_edge("C", "B", weight=1)
    g.add_edge("D", "B", weight=1)
    g.add_edge("E", "B", weight=4)
    g.add_edge("F", "B", weight=4)

    g.add_edge("D", "C", weight=4)
    g.add_edge("E", "C", weight=1)
    g.add_edge("F", "C", weight=4)

    g.add_edge("E", "D", weight=4)
    g.add_edge("F", "D", weight=4)

    g.add_edge("F", "E", weight=1)

    assert 1 == find_optimal_path(g, "A", "F")

def test_4_stations_indirect_varied_weights():
    g = nx.Graph()
    g.add_node("A")

    g.add_edge("B", "A", weight=8)
    g.add_edge("C", "A", weight=8)
    g.add_edge("D", "A", weight=1)
    g.add_edge("E", "A", weight=8)
    g.add_edge("F", "A", weight=8)

    g.add_edge("C", "B", weight=3)
    g.add_edge("D", "B", weight=2)
    g.add_edge("E", "B", weight=8)
    g.add_edge("F", "B", weight=8)

    g.add_edge("D", "C", weight=8)
    g.add_edge("E", "C", weight=4)
    g.add_edge("F", "C", weight=8)

    g.add_edge("E", "D", weight=8)
    g.add_edge("F", "D", weight=8)

    g.add_edge("F", "E", weight=5)

    assert 5 == find_optimal_path(g, "A", "F")

def test_4_stations_indirect_more_varied_weights():
    g = nx.Graph()
    g.add_node("A")

    g.add_edge("B", "A", weight=8)
    g.add_edge("C", "A", weight=8)
    g.add_edge("D", "A", weight=5)
    g.add_edge("E", "A", weight=8)
    g.add_edge("F", "A", weight=8)

    g.add_edge("C", "B", weight=3)
    g.add_edge("D", "B", weight=4)
    g.add_edge("E", "B", weight=8)
    g.add_edge("F", "B", weight=8)

    g.add_edge("D", "C", weight=8)
    g.add_edge("E", "C", weight=2)
    g.add_edge("F", "C", weight=8)

    g.add_edge("E", "D", weight=8)
    g.add_edge("F", "D", weight=8)

    g.add_edge("F", "E", weight=1)

    assert 5 == find_optimal_path(g, "A", "F")
