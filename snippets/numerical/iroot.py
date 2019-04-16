def iroot(a, n=2):
    if a < 2:
        return a

    c = 1
    d = ((n - 1) * c + a // (c**(n - 1))) // n
    e = ((n - 1) * d + a // (d**(n - 1))) // n

    while (c != d) and (c != e):
        c, d, e = d, e, ((n - 1) * e + a // (e**(n - 1))) // n

    return min(d, e)
