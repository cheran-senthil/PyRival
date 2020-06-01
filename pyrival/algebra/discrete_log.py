def discrete_log(a, b, mod):
    """returns the smallest x >= 0 s.t. pow(a, x, mod) == b or None if no such x exists"""
    n = int(mod**0.5) + 1

    # small_step[x] = maximum j <= n s.t. b * a^j % mod = x
    small_step, e = {}, 1
    for j in range(n + 1):
        if e == b:
            return j
        small_step[b * e % mod] = j
        e = e * a % mod

    # find (i, j) s.t. a^(n * i) % mod = b * a^j % mod
    e = factor = pow(a, n, mod)
    for i in range(2, n + 1):
        e = e * factor % mod
        j = small_step.get(e, None)
        if j is not None:
            return n * i - j if pow(a, n * i - j, mod) == b else None

    return None
