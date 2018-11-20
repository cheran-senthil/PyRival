import sys


def read_ints():
    numb, sign = 0, 1

    for char in sys.stdin.read():
        if char >= '0':
            numb = 10 * numb + ord(char) - 48
        else:
            if char == '-':
                sign = -1
            else:
                yield sign * numb
                numb, sign = 0, 1

    if char >= '0':
        yield sign * numb
