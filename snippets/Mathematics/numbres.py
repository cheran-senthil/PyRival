from functools import reduce
from math import factorial
from operator import mul


fib = lambda n: reduce(lambda x, n: (x[1], x[0] + x[1]), range(n), (0, 1))[0]


nCr = lambda n, r: reduce(mul, range(n-r+1, n+1), 1)//factorial(r)


cat = lambda n: nCr(2*n, n)


euler = lambda n, k: sum(((-1)**j) * nCr(n + 1, j) * ((k + 1 - j)**n) for j in range(k + 1))


stirling_2 = lambda n, k: sum(((-1)**(k - j)) * nCr(k, j) * (j**n) for j in range(k + 1)) // factorial(k)
