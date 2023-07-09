# NTT implementation based on https://codeforces.com/blog/entry/117947

# NTT prime
MOD = (119 << 23) + 1
assert MOD & 1

non_quad_res = 2
while pow(non_quad_res, MOD//2, MOD) != MOD - 1:
    non_quad_res += 1
rt = [1]

def ntt(P):
    n = len(P)
    P = list(P)
    assert n and (n - 1) & n == 0
    
    while 2 * len(rt) < n:
        # 4*len(rt)-th root of unity
        root = pow(non_quad_res, MOD // (4*len(rt)), MOD)
        rt.extend([r * root % MOD for r in rt])

    k = n
    while k > 1:
        for i in range(n//k):
            r = rt[i]
            for j1 in range(i*k, i*k + k//2):
                j2 = j1 + k//2
                z = r * P[j2]
                P[j2] = (P[j1] - z) % MOD
                P[j1] = (P[j1] + z) % MOD
        k //= 2
    
    rev = [0] * n
    for i in range(1, n):
        rev[i] = rev[i // 2] // 2 + (i & 1) * n // 2
    return [P[r] for r in rev]

def intt(P):
    n = len(P)
    ninv = pow(n, MOD - 2, MOD)
    return ntt([P[-i] * ninv % MOD for i in range(n)])

def ntt_conv(P, Q):
    m = len(P) + len(Q) - 1
    n = 1 << m.bit_length()

    P = P + [0] * (n - len(P))
    Q = Q + [0] * (n - len(Q))
    P, Q = ntt(P), ntt(Q)

    return intt([p * q % MOD for p,q in zip(P, Q)])[:m]
