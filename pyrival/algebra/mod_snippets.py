"""
A template for useful stuff involving prime modulo computations.

It contains:
1. Calculation of factorial, inverse factorial and modular inverse
   for all integers < maxN in O(maxN) time. Requires maxN <= MOD.

2. Calculate n choose k in O(1) time using precalculated fac and inv_fac.
   Requires n < maxN <= MOD.

3. Calculate n choose k using Lucas theorem in O(log_MOD(n)) time.
   Requires maxN == MOD.

4. Multiply matrices.

5. Multiply matrix vector.

6. Matrix powers using exponentiation by squaring.
"""
MOD = 10 ** 9 + 7 # needs to be prime!
maxN = 10 ** 6
assert maxN <= MOD

modmul = lambda a,b,c=0:(a*b + c) % MOD

""" Precalculate factorial, inverse factorial and modular inverse """

def mod_precalc(n):
    """ Calculates fac, inv_fac and (modular) inv for i < n in O(n) time """
    assert n <= MOD
    
    fac = [1] * n
    for i in range(2, n):
        fac[i] = modmul(fac[i - 1], i)

    inv_fac = [pow(fac[-1], MOD - 2, MOD)] * n
    for i in reversed(range(1, n)):
        inv_fac[i - 1] = modmul(inv_fac[i], i)

    inv = [modmul(inv_fac[i], fac[i - 1]) for i in range(n)]

    return fac, inv_fac, inv

fac, inv_fac, inv = mod_precalc(maxN)


""" Useful functions involving modulo """

def choose(n, k):
    """ Calculate n choose k in O(1) time """
    if k < 0 or k > n:
        return 0
    return modmul(modmul(fac[n], inv_fac[k]), inv_fac[n - k])

def choose_lucas(n, k):
    """ Calculate n choose k in O(log_MOD(n)) time using Lucas thm """
    assert maxN == MOD
    if k < 0 or k > n:
        return 0
    n1, n2 = divmod(n, MOD)
    k1, k2 = divmod(k, MOD)    
    ret = choose(n2, k2) 
    if n1 or k1:
        ret = modmul(ret, choose_lucas(n1, k1))
    return ret

def matrix_modmul(A, B):
    """ Multiplies matrices A and B mod MOD"""
    assert len(A[0]) == len(B)
    C = []
    for Ai in A:
        tmp = [0] * len(B[0])
        for k in range(len(B)):
            Aik = Ai[k]
            Bk = B[k]
            for j in range(len(Bk)):
                tmp[j] = modmul(Aik, Bk[j], tmp[j])
        C.append(tmp)
    return C

def matrix_vec_modmul(A, b):
    """Multiplies matrix A and vector b mod MOD"""
    assert len(A[0]) == len(b)
    res = []
    for Ai in A:
        tmp = 0
        for k in range(len(b)):
            tmp = modmul(Ai[k], b[k], tmp)
        res.append(tmp)
    return res

def matrix_modpow(A, power):
    n = len(A)
    assert n == len(A[0])
    assert power >= 0
    
    res = [[+(i == j) for j in range(n)] for i in range(n)]

    while power:
        if power & 1:
            res = matrix_modmul(res, A)
        power //= 2
        A = power and matrix_modmul(A, A)
    return res
