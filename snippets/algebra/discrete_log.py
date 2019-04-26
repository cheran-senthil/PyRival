def discrete_log(a, b, m):
    """returns some x s.t. pow(a, x, m) == b or None if no such x exists"""
    a %= m
    b %= m
    if b == 1:
        return 0

    n, vals = int(m ** 0.5) + 1, dict()
    mult, cur = pow(a, n, m), 1
    for i in range(n):
        cur = (cur * mult) % m
        vals[cur] = i + 1

    cur = b
    for i in range(n + 1):
        it = vals.get(cur, None)
        if it is not None:
            return it * n - i  # % phi(m)
        cur = (cur * a) % m
    return None
