#!/usr/bin/env python3

import fileinput
import math
import networkx as nx

class Coordinate:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return "(%s, %s, %s)" % (self.x, self.y, self.z)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __hash__(self):
        return int(self.x * 100 + self.y * 100 + self.z * 100)

def parse_coordinate(str):
    x, y, z = [float(x) for x in str.split(" ")]

    return Coordinate(x, y, z)

def distance(c1, c2):
    return round(math.sqrt((c1.x - c2.x) ** 2 + (c1.y - c2.y) ** 2 + (c1.z - c2.z) ** 2), 2)

def add_to_graph(g, new_node):
    existing_nodes = list(g.nodes())

    for node in existing_nodes:
        g.add_edge(new_node, node, weight=distance(new_node, node))

#def print_graph(g):
#    print(g.nodes())
#    for edge in g.edges():
#        print("%s %s" % (edge, g.get_edge_data(edge[0], edge[1])))
#
def next(unvisited, priority_queue):
    weight = math.inf
    next_node = None

    for node in unvisited:
        if (priority_queue[node] < weight):
            weight = priority_queue[node]
            next_node = node

    return next_node

def find_optimal_path(g, origin, destination):
    unvisited = set(g.nodes())
    priority_queue = {}

    for node in unvisited:
        priority_queue[node] = math.inf

    priority_queue[origin] = 0
    #print("unvisited =\t", unvisited)
    #print("priority_queue =", priority_queue)
    while (unvisited):
        node = next(unvisited, priority_queue)
        #print("next =\t\t", node)

        if (node == destination):
            return priority_queue[node]

        for neighbor in g.neighbors(node):
            if (neighbor not in unvisited):
                continue

            #print("neighbor =\t", neighbor)
            weight = g.get_edge_data(node, neighbor)["weight"]
            if (weight < priority_queue[neighbor]):
                priority_queue[neighbor] = max(weight, priority_queue[node])

        unvisited.remove(node)
        #print("unvisited =\t", unvisited)
        #print("priority_queue =", priority_queue)
        #print("---")

def main():
    station_count = 0

    earth = Coordinate(0.0, 0.0, 0.0)
    zearth = None

    g = nx.Graph()
    g.add_node(earth)

    for line in fileinput.input():
        if (fileinput.isfirstline()):
            zearth = parse_coordinate(line)
            add_to_graph(g, zearth)

        if (fileinput.lineno() == 2):
            station_count = int(line)

        if (fileinput.lineno() > 2):
            station = parse_coordinate(line)
            add_to_graph(g, station)

        if (fileinput.lineno() > station_count + 1):
            break

    longest_jump_in_optimal_path = find_optimal_path(g, earth, zearth)

    print(longest_jump_in_optimal_path)

if __name__ == "__main__":
    main()
