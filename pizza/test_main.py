from subprocess import Popen, PIPE

given_test_data = """5 2
3 3 2
1 1 2"""

empty_city = ""

single_pizzeria = """10 1
3 5 2"""

uniform_distribution = """3 9
1 1 0
1 2 0
1 3 0
2 1 0
2 2 0
2 3 0
3 1 0
3 2 0
3 3 0"""

on_the_same_block = """5 3
3 3 0
3 3 1
3 3 2"""

past_bottom_left_edge = """10 2
1 1 5
2 2 8"""

past_top_right_edge = """10 2
10 10 5
9 9 8"""

too_many_pizzerias = """5 1
3 3 2
1 2 3
4 5 6
7 8 9"""

large_pizzeria = """5 1
3 3 1000
"""

large_city = """1000 5
10 5 100
34 67 55
448 765 31
806 765 300
313 702 140"""

def run_test(data):
    process = Popen(["./main.py"], stdin=PIPE, stdout=PIPE)
    stdout = process.communicate(input=data.encode())[0]

    return int(stdout.decode())

def test_given_test_data():
    assert run_test(given_test_data) == 2

def test_empty_city():
    assert run_test(empty_city) == 0

def test_single_pizzeria():
    assert run_test(single_pizzeria) == 1

def test_uniform_distribution():
    assert run_test(uniform_distribution) == 1

def test_on_the_same_block():
    assert run_test(on_the_same_block) == 3

def test_past_bottom_left_edge():
    assert run_test(past_bottom_left_edge) == 2

def test_past_top_right_edge():
    assert run_test(past_top_right_edge) == 2

def test_too_many_pizzerias():
    assert run_test(too_many_pizzerias) == 1

def test_large_pizzeria():
    assert run_test(large_pizzeria) == 1

def test_large_city():
    assert run_test(large_city) == 2
