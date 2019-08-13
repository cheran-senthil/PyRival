MOD = 10**9 + 7


def berlekamp_massey(s):
    n = len(s)
    L, m = 0, 0
    C, B, T = [0] * n, [0] * n, []
    C[0], B[0] = 1, 1

    b = 1
    for i in range(n):
        m += 1
        d = s[i] % MOD
        for j in range(1, L + 1):
            d = (d + C[j] * s[i - j]) % MOD

        if not d:
            continue

        T = C[:]
        coef = (d * pow(b, MOD - 2, MOD)) % MOD
        for j in range(m, n):
            C[j] = (C[j] - coef * B[j - m]) % MOD
        if 2 * L > i:
            continue
        L = i + 1 - L
        B, b, m = T[:], d, 0

    return [-C[i] % MOD for i in range(1, L + 1)]


def linear_rec(S, tr, k):
    n = len(S)

    def combine(a, b):
        res = [0] * (2 * n + 1)
        for i in range(n + 1):
            for j in range(n + 1):
                res[i + j] = (res[i + j] + a[i] * b[j]) % MOD

        for i in range(2 * n, n, -1):
            for j in range(n):
                res[i - 1 - j] = (res[i - 1 - j] + res[i] * tr[j]) % MOD
        return res[:n + 1]

    pol, e = [0] * (n + 1), [0] * (n + 1)
    pol[0], e[1] = 1, 1

    k += 1
    while k:
        if k & 1:
            pol = combine(pol, e)
        e = combine(e, e)
        k >>= 1

    res = 0
    for i in range(n):
        res = (res + pol[i + 1] * S[i]) % MOD
    return res
