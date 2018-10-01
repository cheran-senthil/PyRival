from copy import deepcopy


def gauss(A, b):
    # returns det(A), x s.t. Ax = b
    a = deepcopy(A)
    x = deepcopy(b)
    n = len(a)
    p = len(x[0])

    determinant = 1
    for i in range(n - 1):
        k = i
        for j in range(i + 1, n):
            if abs(a[j][i]) > abs(a[k][i]):
                k = j
        if k != i:
            a[i], a[k] = a[k], a[i]
            x[i], x[k] = x[k], x[i]
            determinant = -determinant

        for j in range(i + 1, n):
            t = a[j][i] / a[i][i]
            for k in range(i + 1, n):
                a[j][k] -= t * a[i][k]
            for k in range(p):
                x[j][k] -= t * x[i][k]

    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            t = a[i][j]
            for k in range(p):
                x[i][k] -= t * x[j][k]
        t = 1 / a[i][i]
        determinant *= a[i][i]
        for j in range(p):
            x[i][j] *= t

    return determinant, x
