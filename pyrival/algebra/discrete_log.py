def discrete_log(a, b, mod):
    """returns the smallest x >= 0 s.t. pow(a, x, mod) == b or None if no such x exists"""
    m = int(mod**0.5) + 1

    # small_step[x] = minimum j <= m s.t. b * a^j % mod = x
    small_step, e = {}, 1
    for j in range(m + 1):
        if e == b:
            return j
        small_step[b * e % mod] = j
        e = e * a % mod

    # find (i, j) s.t. a^(m * i) % mod = b * a^j % mod
    e = factor = pow(a, m, mod)
    for i in range(2, m + 1):
        e = e * factor % mod
        j = small_step.get(e, None)
        if j is not None:
            return m * i - j if pow(a, m * i - j, mod) == b else None

    return None
