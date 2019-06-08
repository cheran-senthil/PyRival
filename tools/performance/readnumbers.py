import sys


def readnumbers(zero=0):
    _ord = ord if round(0.5) else lambda x: x

    nums = []
    num, neg = zero, False
    i, s = 0, sys.stdin.buffer.read()
    try:
        while True:
            if s[i] >= b'0' [0]:
                num = 10 * num + _ord(s[i]) - 48
            elif s[i] == b'-' [0]:
                neg = True
            elif s[i] != b'\r' [0]:
                nums.append(-num if neg else num)
                num, neg = zero, False
            i += 1
    except KeyError:
        pass

    if s and s[-1] >= b'0' [0]:
        nums.append(-num if neg else num)
    return nums
