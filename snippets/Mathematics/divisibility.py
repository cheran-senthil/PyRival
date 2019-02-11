from functools import reduce
from math import gcd

gcdm = lambda *args: reduce(gcd, args, 0)

lcm = lambda a, b: a * b // gcd(a, b)

lcmm = lambda *args: reduce(lcm, args, 1)
