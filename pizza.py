#!/usr/bin/env python3

import fileinput

def parse_ints(str):
    return [int(x) for x in str.split(" ")]

def create_city(city_dimension):
    return [[0 for x in range(city_dimension)] for y in range(city_dimension)]

def pizzeria_area(x, y, k):
    return [
        (potential_x, potential_y)
        for potential_x in range(x - k, x + k + 1)
        for potential_y in range(y - k, y + k + 1)
        if (abs(x - potential_x) + abs(y - potential_y) <= k)
    ]

def print_map(city):
    for line in city[::-1]:
        print(line)

def main():
    highest_density = 0

    for line in fileinput.input():
        if (fileinput.isfirstline()):
            city_dimension, pizzeria_count = parse_ints(line)
            city = create_city(city_dimension)
            continue

        pizzeria_x, pizzeria_y, k = parse_ints(line)
        area = pizzeria_area(pizzeria_x, pizzeria_y, k)

        for coordinate in area:
            x = coordinate[0] - 1
            y = coordinate[1] - 1

            if (0 <= x < city_dimension and 0 <= y < city_dimension):
                city[x][y] += 1

                if (city[x][y] > highest_density):
                    highest_density = city[x][y]

        if (fileinput.lineno() > pizzeria_count):
            break

    print(highest_density)

if __name__ == "__main__":
    main()
