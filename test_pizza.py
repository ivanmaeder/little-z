from subprocess import Popen, PIPE

given_test_data = """5 2
3 3 2
1 1 2"""

def run_test(data):
    process = Popen(["./pizza.py"], stdin=PIPE, stdout=PIPE)
    stdout = process.communicate(input=data.encode())[0]

    return int(stdout.decode())

def test_given_test_data():
    assert run_test(given_test_data) == 2
