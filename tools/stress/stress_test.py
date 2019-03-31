from stress import stress
import subprocess


def testcase_generator():
    for i in range(1, 10):
        yield '{}\n'.format(i)


def solution(inp):
    proc = subprocess.run(['python', 'solution.py'], input=inp, text=True, capture_output=True)
    return proc.stdout, proc.stderr


def checker(inp, out):
    #proc = subprocess.run(['python', 'checker.py'], input=inp, text=True, capture_output=True)
    #return proc.stdout == out

    i = [0, 1]

    for _ in range(int(inp) - 1):
        i[0], i[1] = i[1], i[0] + i[1]

    return int(out) == i[1]

stress(testcase_generator, solution, checker)
