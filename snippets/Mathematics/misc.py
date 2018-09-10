from operator import mul
from math import factorial, gcd
from functools import reduce

def nCr(n, r):
    return reduce(mul, range(n-r+1, n+1), 1)//factorial(r)

def cat(n):
    return nCr(2*n, n)

def mul_inv(a, p):
    return pow(a, p-2, p)

def lcm(a, b):
    return a * b // gcd(a, b)

def lcmm(*args):
    return reduce(lcm, args)