def discrete_log(a, b, m):
    n = int(m**0.5) + 1

    an = 1
    for i in range(n):
        an = (an * a) % m

    vals = dict()

    cur = an
    for i in range(1, n + 1):
        if cur not in vals:
            vals[cur] = i
        cur = (cur * an) % m

    cur = b
    for i in range(n + 1):
        if cur in vals:
            ans = vals[cur] * n - i
            if ans < m:
                return ans
        cur = (cur * a) % m

    return -1
