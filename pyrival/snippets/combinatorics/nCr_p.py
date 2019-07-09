MOD = 10**9 + 7

MAXN = 2 * 10**5

fact, inv_fact = [0] * (MAXN + 1), [0] * (MAXN + 1)
fact[0] = 1
for i in range(MAXN):
    fact[i + 1] = fact[i] * (i + 1) % MOD

inv_fact[-1] = pow(fact[-1], MOD - 2, MOD)
for i in reversed(range(MAXN)):
    inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD


def nCr_mod(n, r):
    res = 1
    while n or r:
        a, b = n % MOD, r % MOD
        if a < b:
            return 0
        res = res * fact[a] % MOD * inv_fact[b] % MOD * inv_fact[a - b] % MOD
        n //= MOD
        r //= MOD
    return res
