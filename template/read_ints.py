import sys


def read_ints():
    """Read integers from underlying buffer until we hit EOF."""
    numb, sign = 0, 1
    res = []

    s = sys.stdin.read()
    for i in range(len(s)):
        if s[i] >= '0':
            numb = 10 * numb + ord(s[i]) - 48
        else:
            if s[i] == '-':
                sign = -1
            else:
                res.append(sign * numb)
                numb, sign = 0, 1

    if s[-1] >= '0':
        res.append(sign * numb)

    return res
