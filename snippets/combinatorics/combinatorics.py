import math
import operator as op
from functools import reduce


def memoize(f):
    """memoization decorator for a function taking one or more arguments"""

    class memodict(dict):
        def __getitem__(self, *key):
            return dict.__getitem__(self, key)

        def __missing__(self, key):
            ret = self[key] = f(*key)
            return ret

    return memodict().__getitem__


@memoize
def catalan_recursive(n):
    if n == 0:
        return 1
    return (2 * (2 * n - 1) * catalan_recursive(n - 1)) // (n + 1)


@memoize
def euler_recursive(n, k):
    if (k == 0) or (n - 1 == k):
        return 1
    return (n - k) * euler_recursive(n - 1, k - 1) + (k + 1) * euler_recursive(n - 1, k)


@memoize
def stirling_1_recursive(n, k):
    if (n == k == 0):
        return 1
    if (n == 0) or (k == 0):
        return 0
    return stirling_1_recursive(n - 1, k - 1) + (n - 1) * stirling_1_recursive(n - 1, k)


@memoize
def stirling_2_recursive(n, k):
    if (k == 1) or (n == k):
        return 1
    return stirling_2_recursive(n - 1, k - 1) + k * stirling_2_recursive(n - 1, k)


nCr = lambda n, r: reduce(op.mul, range(n - r + 1, n + 1), 1) // math.factorial(r)

multinomial = lambda k: math.factorial(sum(k)) // reduce(op.mul, (math.factorial(i) for i in k))

derangements = lambda n: int(math.factorial(n) / math.e + 0.5)

bell = lambda n: sum(stirling_2_recursive(k, n) for k in range(n + 1))

catalan = lambda n: nCr(2 * n, n) // (n + 1)

euler = lambda n, k: sum((1 - 2 * (j & 1)) * nCr(n + 1, j) * ((k + 1 - j)**n) for j in range(k + 1))

stirling_2 = lambda n, k: sum(((-1)**(k - j)) * nCr(k, j) * (j**n) for j in range(k + 1)) // math.factorial(k)
