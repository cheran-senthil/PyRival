def factorial_p(n, p):
    ans = 1
    if n <= p // 2:
        for i in range(1, n + 1):
            ans = (ans * i) % p
    else:
        for i in range(1, p - n):
            ans = (ans * i) % p
        ans = pow(ans, p - 2, p)
        if n % 2 == 0:
            ans = p - ans
    return ans


def nCr_p(n, r, p):
    ans = 1
    while (n != 0) or (r != 0):
        a, b = n % p, r % p
        if a < b:
            return 0
        ans = (ans * factorial_p(a, p) * pow(factorial_p(b, p), p - 2, p) * pow(factorial_p(a - b, p), p - 2, p)) % p
        n //= p
        r //= p
    return ans
