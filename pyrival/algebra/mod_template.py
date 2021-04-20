"""
A template for usefull stuff involving prime modulo. It contains:
1. Fast calculation of (a * b + c) % MOD (Especially usefull for PyPy users on windows).
2. Calculation of factorial, inverse factorial and modular inverse
   for all integers < maxN in O(maxN) time.
3. Calculate n choose k in O(1) time using precalculated fac. and inv. fac.
4. Multiply matrices mod MOD.
"""
MOD = 10 ** 9 + 7 # needs to be prime!
maxN = 10 ** 6    # needs to be <= MOD


def fast_modder(MOD):
    """ Returns a function modmul(a,b,c=0) that quickly calculates (a * b + c) % MOD, assuming 0 <= a,b < MOD """
    import sys, platform
    impl = platform.python_implementation()
    maxs = sys.maxsize
    if 'PyPy' in impl and MOD <= maxs and MOD ** 2 > maxs:
        import __pypy__
        intsub = __pypy__.intop.int_sub
        intmul = __pypy__.intop.int_mul
        intmulmod = __pypy__.intop.int_mulmod
        if MOD < 2**30 - 1000:
            MODINV = 1.0 / MOD
            def modmul(a, b, c=0):
                return (intsub(intmul(a,b), intmul(MOD, int(MODINV * a * b))) + c) % MOD
        else:
            def modmul(a, b, c=0):
                return (intmulmod(a, b, MOD) + c) % MOD
    else:
        def modmul(a, b, c=0):
            return (a * b + c) % MOD
    return modmul

modmul = fast_modder(MOD)


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
    return modmul(modmul(fac[n], fac_inv[k]), fac_inv[n - k])

def matrix_modmul(A, B):
    """ Multiplies matrices A and B, assuming 0 <= A[i][j], B[i][j] < MOD """
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
