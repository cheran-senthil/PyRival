def is_prime(n):
    """returns True if n is prime else False"""
    if n < 2 or n % 6 % 4 != 1:
        return n - 2 < 2
    s = ((n - 1) & (1 - n)).bit_length() - 1
    d = n >> s
    for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
        p, i = pow(a, d, n), s
        while p != 1 and p != n - 1 and a % n and i:
            i -= 1
            p = (p * p) % n
        if p != n - 1 and i != s:
            return False
    return True
