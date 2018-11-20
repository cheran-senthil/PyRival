import sys


def read_ints():
    s = sys.stdin.read()
    numb, sign = 0, 1

    res = []
    res_append = res.append

    for i in range(len(s)):
        if s[i] >= '0':
            numb = 10 * numb + ord(s[i]) - 48
        else:
            if s[i] == '-':
                sign = -1
            else:
                res_append(sign * numb)
                numb, sign = 0, 1

    if s[-1] >= '0':
        res_append(sign * numb)

    return res
