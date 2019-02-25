from subprocess import Popen, PIPE

given_test_data1 = """2.00 2.00 2.00
3
0.00 0.00 2.00
0.00 2.00 2.00
2.00 0.00 0.00"""

given_test_data2 = """2.00 2.00 2.00
3
1.00 1.00 1.00
1.00 2.00 2.00
2.00 2.00 1.00"""

single_hop = """2.00 2.00 2.00
0"""

single_stopover = """2.00 2.00 2.00
1
1.00 1.00 1.00"""

def run_test(data):
    process = Popen(["./main.py"], stdin=PIPE, stdout=PIPE)
    stdout = process.communicate(input=data.encode())[0]

    return float(stdout.decode())

def test_given_test_data1():
    assert 2.00 == run_test(given_test_data1)

def test_given_test_data2():
    assert 1.73 == run_test(given_test_data2)

def test_single_hop():
    assert 3.46 == run_test(single_hop)

def test_single_stopover():
    assert 1.73 == run_test(single_stopover)
