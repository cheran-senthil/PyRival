def ntt(a, mod=998244353, root=3, inv=False):
    n = len(a)
    w = [1] * (n >> 1)

    w[1] = pow(root, (mod - 1) // n, mod)
    if inv:
        w[1] = pow(w[1], mod - 2, mod)

    for i in range(2, (n >> 1)):
        w[i] = w[i - 1] * w[1] % mod

    rev = [0] * n
    for i in range(n):
        rev[i] = rev[i >> 1] >> 1
        if i & 1:
            rev[i] |= (n >> 1)
        if i < rev[i]:
            a[i], a[rev[i]] = a[rev[i]], a[i]

    step = 2
    while step <= n:
        half, diff = step >> 1, n // step
        for i in range(0, n, step):
            pw = 0
            for j in range(i, i + half):
                v = a[j + half] * w[pw] % mod
                a[j + half] = a[j] - v if a[j] - v >= 0 else a[j] - v + mod
                a[j] = a[j] + v if a[j] + v < mod else a[j] + v - mod
                pw += diff

        step <<= 1

    if inv:
        inv_n = pow(n, mod - 2, mod)
        for i in range(n):
            a[i] = a[i] * inv_n % mod


def conv(a, b, mod=998244353, root=3):
    s = len(a) + len(b) - 1
    n = 1 << s.bit_length()

    fa = a + [0] * (n - len(a))
    fb = b + [0] * (n - len(b))

    ntt(fa, mod=mod, root=root)
    ntt(fb, mod=mod, root=root)

    for i in range(n):
        fa[i] *= fb[i]

    ntt(fa, mod=mod, root=root, inv=True)

    return [fa[i].real for i in range(s)]
