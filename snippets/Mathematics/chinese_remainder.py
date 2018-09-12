from functools import reduce
from operator import mul


def chinese_remainder(a, n):
    # solve for x = a_i (mod n_i) where n_i is prime
    x = 0
    prod = reduce(mul, n)

    for a_i, n_i in zip(a, n):
        p = prod // n_i
        x += a_i * pow(p, n_i - 2, n_i) * p

    return x % prod
