def discrete_log(a, b, mod):
    """
    Returns smallest x >= 0 s.t. pow(a, x, mod) == b or None if no such x exists. 
    Note: works even if a and mod are not coprime.
    """
    n = int(mod**0.5) + 1

    # tiny_step[x] = maximum j <= n s.t. b * a^j % mod = x
    tiny_step, e = {}, 1 % mod
    for j in range(n + 1):
        if e == b:
            return j
        tiny_step[b * e % mod] = j
        e = e * a % mod

    # find (i, j) s.t. a^(n * i) % mod = b * a^j % mod
    e = factor = pow(a, n, mod)
    for i in range(2, n + 1):
        e = e * factor % mod
        if e in tiny_step:
            j = tiny_step[e]
            return n * i - j if pow(a, n * i - j, mod) == b else None
