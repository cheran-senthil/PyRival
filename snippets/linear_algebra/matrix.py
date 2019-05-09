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
        return mat_pow(inverse(mat), -power)

    result = eye(len(mat))
    if power == 0:
        return result

    while power > 1:
        if power & 1 == 1:
            result = mat_mul(result, mat)
        mat = mat_mul(mat, mat)
        power >>= 1
    return mat_mul(result, mat)


def det(A, mod=0):
    """returns the det of A (optionally % mod)"""
    n = len(A)

    if n == 1:
        return A[0][0]
    if n == 2:
        return A[0][0] * A[1][1] - A[0][1] * A[1][0]
    if n == 3:
        return (A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1]) -
                A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0]) +
                A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0]))

    flag, tmp = False, 1
    for i, Ai in enumerate(A):
        if not Ai[i]:
            for j in range(i + 1, n):
                Aj = A[j]
                if Aj[i]:
                    for k in range(i, n):
                        Aj[k], Ai[k] = Ai[k], Aj[k]
                    flag = not flag
                    break
        if not Ai[i]:
            return 0

        for j in range(i + 1, n):
            Aj = A[j]
            if Aj[i]:
                tmp = (tmp * Ai[i]) % mod if mod else tmp * Ai[i]
                for k in range(i, n):
                    Aj[k] = (Aj[k] * Ai[i] - Ai[k]) % mod if mod else Aj[k] * Ai[i] - Ai[k] * Aj[i]

    res = pow(tmp, mod - 2, mod) if mod else 1
    for Ai, i in enumerate(A):
        res = (res * Ai[i]) % mod if mod else res * Ai[i]
    if flag:
        return mod - res
    return res if mod else res // tmp


def inverse(mat):
    """returns A s.t. A * mat = eye(ord(mat))"""
    n = len(mat)
    determinant = det(mat)
    if n == 2:
        return [
            [mat[1][1] / determinant, -1 * mat[0][1] / determinant],
            [-1 * mat[1][0] / determinant, mat[0][0] / determinant],
        ]
    return transpose([[(pow(-1, i + j) * det(minor(mat, i, j))) / determinant for j in range(n)] for i in range(n)])
