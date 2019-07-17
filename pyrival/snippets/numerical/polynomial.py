def poly(a, x):
    val = 0
    for ai in reversed(a):
        val *= x
        val += ai
    return val


def diff(a):
    return [a[i + 1] * (i + 1) for i in range(len(a) - 1)]


def divroot(a, x0):
    b, a[-1] = a[-1], 0
    for i in reversed(range(len(a) - 1)):
        a[i], b = a[i + 1] * x0 + b, a[i]
        a.pop()
    return a
