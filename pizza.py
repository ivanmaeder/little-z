#!/usr/bin/env python

import fileinput

def parse_ints(str):
    return [int(x) for x in str.split(" ")]

def parse_first_line(line):
    return parse_ints(line)

def parse_pizzeria_line(line):
    return parse_ints(line)

def create_city(city_dimension):
    return [[0 for x in range(city_dimension)] for y in range(city_dimension)]

def pizzeria_area(x, y, k):
    return [
        (potential_x, potential_y)
        for potential_x in range(x - k, x + k + 1)
        for potential_y in range(y - k, y + k + 1)
        if (abs(x - potential_x) + abs(y - potential_y) <= k)
    ]

def main():
    for line in fileinput.input():
        if fileinput.isfirstline():
            [city_dimension, pizzeria_count] = parse_first_line(line)
            city = create_city(city_dimension)
            continue

        #use pizzeria_count ??

        [x, y, k] = parse_pizzeria_line(line)

        #calculate pizzeria area
        #update city based on area
        #update the highest density number

    print(1)

if __name__ == "__main__":
    main()
