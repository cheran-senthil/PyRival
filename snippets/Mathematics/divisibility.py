from math import gcd

lcm = lambda a, b: a * b // gcd(a, b)


def gcdm(a, *r):
    for b in r:
        a = gcd(a, b)
    return a


def lcmm(a, *r):
    for b in r:
        a = lcm(a, b)
    return a
