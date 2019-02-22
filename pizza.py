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
    result = []
    if (k == 0):
        return [(x, y)]
    if (k == 1):
        result.append((x, y + k))
        result.append((x - k, y))
        result.append((x, y))
        result.append((x + k, y))
        result.append((x, y - k))
    if (k == 2):
        result.append((x, y + k))

        result.extend([(x - 1, y + 1), (x, y + 1), (x + 1, y + 1), (x - 2, y), (x - 1, y), (x, y), (x + 1, y), (x + 2, y), (x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x, y - k)])

    return result

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
