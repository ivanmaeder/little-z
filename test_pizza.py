from subprocess import Popen, PIPE

given_test_data = """5 2
3 3 2
1 1 2"""

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

def run_test(data):
    process = Popen(["./pizza.py"], stdin=PIPE, stdout=PIPE)
    stdout = process.communicate(input=data.encode())[0]

    return int(stdout.decode())

def test_given_test_data():
    assert run_test(given_test_data) == 2

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
