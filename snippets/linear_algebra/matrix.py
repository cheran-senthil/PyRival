from copy import deepcopy

transpose = lambda mat: [list(col) for col in zip(*mat)]

minor = lambda mat, i, j: [row[:j] + row[j + 1:] for row in (mat[:i] + mat[i + 1:])]

mat_add = lambda *mat: [[sum(elements) for elements in zip(*row)] for row in zip(*mat)]

mat_sub = lambda A, B: [[i - j for i, j in zip(*row)] for row in zip(A, B)]

mat_mul = lambda A, B: [[sum(i * j for i, j in zip(row, col)) for col in zip(*B)] for row in A]

vec_mul = lambda mat, vec: [sum(a * b for a, b in zip(row, vec)) for row in mat]


def eye(m):
    """returns an indentity matrix of order m"""
    identity = [[0] * m for _ in range(m)]
    for i, row in enumerate(identity):
        row[i] = 1
    return identity


def mat_pow(mat, power):
    """returns mat**power"""
    if power < 0:
        return mat_pow(mat_inv(mat), -power)

    result = eye(len(mat))
    if power == 0:
        return result

    while power > 1:
        if power & 1 == 1:
            result = mat_mul(result, mat)
        mat = mat_mul(mat, mat)
        power >>= 1
    return mat_mul(result, mat)


def mat_inv(A):
    B = deepcopy(A)
    n = len(A)
    col = list(range(n))

    tmp = [[0] * n for _ in range(n)]
    for i in range(n):
        tmp[i][i] = 1

    for i in range(n):
        r = c = i
        for j in range(i, n):
            for k in range(i, n):
                if abs(B[j][k]) > abs(B[r][c]):
                    r, c = j, k
        if B[r][c] == 0:
            return B

        B[i], B[r] = B[r], B[i]
        tmp[i], tmp[r] = tmp[r], tmp[i]
        for j in range(n):
            B[j][i], B[j][c] = B[j][c], B[j][i]
            tmp[j][i], tmp[j][c] = tmp[j][c], tmp[j][i]
        col[i], col[c] = col[c], col[i]
        v = B[i][i]
        for j in range(i + 1, n):
            f = B[j][i] / v
            B[j][i] = 0
            for k in range(i + 1, n):
                B[j][k] -= f * B[i][k]
            for k in range(n):
                tmp[j][k] -= f * tmp[i][k]

        for j in range(i + 1, n):
            B[i][j] /= v

        for j in range(n):
            tmp[i][j] /= v
        B[i][i] = 1

    for i in reversed(range(n)):
        for j in range(i):
            v = B[j][i]
            for k in range(n):
                tmp[j][k] -= v * tmp[i][k]

    for i in range(n):
        for j in range(n):
            B[col[i]][col[j]] = tmp[i][j]
    return B
