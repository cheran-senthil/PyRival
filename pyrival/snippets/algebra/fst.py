import operator as op


def fst(a, oplus=op.and_, inv=False):
    step = 1
    while step < len(a):
        for i in range(0, len(a), 2 * step):
            for j in range(i, i + step):
                if oplus == op.and_:
                    a[j], a[j + step] = a[j + step] - a[j], a[j] if inv else a[j + step], a[j] + a[j + step]
                elif oplus == op.or_:
                    a[j], a[j + step] = a[j + step], a[j] - a[j + step] if inv else a[j] + a[j + step], a[j]
                elif oplus == op.xor:
                    a[j], a[j + step] = a[j] + a[j + step], a[j] - a[j + step]
        step *= 2

    if inv and oplus == op.xor:
        for i in range(len(a)):
            a[i] /= len(a)


def fst_conv(a, b):
    fst(a), fst(b)
    for i in range(len(a)):
        a[i] *= b[i]
    fst(1, inv=True)
    return a
