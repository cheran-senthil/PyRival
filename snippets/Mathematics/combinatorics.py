from functools import reduce
from math import e, factorial
from operator import mul

nCr = lambda n, r: reduce(mul, range(n-r+1, n+1), 1)//factorial(r)

derangements = lambda n: int(factorial(n) / e + 0.5)

cat = lambda n: nCr(2*n, n)

euler = lambda n, k: sum(((-1)**j) * nCr(n + 1, j) * ((k + 1 - j)**n) for j in range(k + 1))

stirling_2 = lambda n, k: sum(((-1)**(k - j)) * nCr(k, j) * (j**n) for j in range(k + 1)) // factorial(k)
