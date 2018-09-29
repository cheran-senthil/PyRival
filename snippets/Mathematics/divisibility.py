from fractions import gcd
from functools import reduce

lcm = lambda a, b: a * b // gcd(a, b)

lcmm = lambda *args: reduce(lcm, args)

gcdm = lambda *args: reduce(gcd, args)

mul_inv = lambda a, p: pow(a, p-2, p)
