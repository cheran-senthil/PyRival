import math


def nCr_p(n, r, p):
    c = 1
    while (n != 0) or (r != 0):
        a, b = n % p, r % p
        if a < b:
            return 0
        c = (c * math.factorial(a) * pow(math.factorial(b), p-2, p) * pow(math.factorial(a - b), p - 2, p)) % p
        n //= p
        r //= p
    return c
