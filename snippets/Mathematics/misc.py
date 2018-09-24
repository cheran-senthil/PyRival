from cmath import sqrt
from fractions import gcd
from functools import reduce
from math import e, factorial


quadratic = lambda a, b, c: ((-b + sqrt(b*b - 4*a*c)) / (2*a), (-b - sqrt(b*b - 4*a*c)) / (2*a))

lcm = lambda a, b: a * b // gcd(a, b)

lcmm = lambda *args: reduce(lcm, args)

gcdm = lambda *args: reduce(gcd, args)

mul_inv = lambda a, p: pow(a, p-2, p)

derangements = lambda n: int(factorial(n) / e + 0.5)
