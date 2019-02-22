import os
import sys

if sys.version_info[0] < 3:
    s = os.read(0, os.fstat(0).st_size)
    res = []

    numb, sign = 0, 1
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

else:
    s = os.read(0, os.fstat(0).st_size)
    res = []

    numb, sign = 0, 1
    for i in range(len(s)):
        if s[i] >= 48:
            numb = 10 * numb + s[i] - 48
        else:
            if s[i] == 45:
                sign = -1
            else:
                res.append(sign * numb)
                numb, sign = 0, 1
    if s[-1] >= 48:
        res.append(sign * numb)
