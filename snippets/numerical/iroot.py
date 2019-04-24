def iroot(n, k=2):
    if n == 0:
        return 0
    if n < 0:
        return -iroot(-n, k) if k & 1 else None
    u, s = n, n + 1
    while u < s:
        s = u
        t = (k - 1) * s + n // s ** (k - 1)
        u = t // k
    return s
