def fst(a, op='AND', inv=False):
    step = 1
    while step < len(a):
        for i in range(0, len(a), 2 * step):
            for j in range(i, i + step):
                if op == 'AND':
                    a[j], a[j + step] = a[j + step] - a[j], a[j] if inv else a[
                        j + step], a[j] + a[j + step]
                elif op == 'OR':
                    a[j], a[j + step] = a[j + step], a[j] - a[
                        j + step] if inv else a[j] + a[j + step], a[j]
                elif op == 'XOR':
                    a[j], a[j + step] = a[j] + a[j + step], a[j] - a[j + step]

        step *= 2

    if inv and (op == 'XOR'):
        for i in range(len(a)):
            a[i] /= len(a)


def conv(a, b):
    fst(a)
    fst(b)

    for i in range(len(a)):
        a[i] *= b[i]

    fst(1, inv=True)

    return a
