from functools import reduce


def gcd(x, y):
    """ greatest common divisor of x and y """
    while y:
        x, y = y, x % y
    return x


gcdm = lambda *args: reduce(gcd, args, 0)

lcm = lambda a, b: a * b // gcd(a, b)

lcmm = lambda *args: reduce(lcm, args, 1)
