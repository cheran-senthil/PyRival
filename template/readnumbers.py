import os
import sys


def readnumbers(var=int):
    """ Read numbers till EOF. Use var to change type. """
    numbers, b = [], os.read(0, os.fstat(0).st_size)

    num, sign = var(0), 1
    for char in b:
        if char >= b'0' [0]:
            num = 10 * num + (ord(char) if sys.version_info[0] < 3 else char) - 48
        elif char == b'-' [0]:
            sign = -1
        elif char != b'\r' [0]:
            numbers.append(sign * num)
            num, sign = var(0), 1

    if b and b[-1] >= b'0' [0]:
        numbers.append(sign * num)

    return numbers
