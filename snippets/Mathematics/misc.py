from fractions import gcd
from functools import reduce
from math import factorial
from operator import mul


fib = lambda n: reduce(lambda x, n: (x[1], x[0] + x[1]), range(n), (0, 1))[0]


nCr = lambda n, r: reduce(mul, range(n-r+1, n+1), 1)//factorial(r)


cat = lambda n: nCr(2*n, n)


lcm = lambda a, b: a * b // gcd(a, b)


lcmm = lambda *args: reduce(lcm, args)


mul_inv = lambda a, p: pow(a, p-2, p)
