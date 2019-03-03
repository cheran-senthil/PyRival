import math

FMOD = 1000000007.0
PREC = 7881299347898367.0
SHRT = 65536.0

fmod = lambda x: x - FMOD * math.trunc(x / FMOD)

transpose = lambda mat: [list(col) for col in zip(*mat)]

minor = lambda mat, i, j: [row[:j] + row[j + 1:] for row in (mat[:i] + mat[i + 1:])]

mat_add = lambda *mat: [[sum(elements) for elements in zip(*row)] for row in zip(*mat)]

mat_sub = lambda A, B: [[i - j for i, j in zip(*row)] for row in zip(A, B)]

mat_mul = lambda A, B: [[sum(i * j for i, j in zip(row, col)) for col in zip(*B)] for row in A]

vec_mul = lambda mat, vec: [sum(a * b for a, b in zip(row, vec)) for row in mat]


def mat_mul_mod(A, B):
    B = [[(Bij - SHRT * math.trunc(Bij / SHRT)) - 1j * (math.trunc(Bij / SHRT)) for Bij in Bi] for Bi in B]
    C = [[0.0] * len(B[0]) for _ in range(len(A))]

    for i, Ai in enumerate(A):
        Ci = C[i]
        for j, Bj in enumerate(B):
            Aij = Ai[j] + 1j * fmod(Ai[j] * SHRT)
            for k, Bjk in enumerate(Bj):
                Ci[k] += (Aij * Bjk).real
                if Ci[k] > PREC:
                    Ci[k] = fmod(Ci[k])

        C[i] = [fmod(Cij) for Cij in Ci]

    return C


def eye(m):
    identity = [[0] * m for _ in range(m)]
    for i, row in enumerate(identity):
        row[i] = 1

    return identity


def mat_pow(mat, power):
    if power < 0:
        return mat_pow(inverse(mat), -power)

    result = eye(len(mat))

    if power == 0:
        return result

    for i in bin(power)[:1:-1]:
        if i == '1':
            result = mat_mul(result, mat)
        mat = mat_mul(mat, mat)

    return result


def det(mat, mod=0):
    n = len(mat)

    if n == 1:
        return mat[0][0]
    if n == 2:
        return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
    if n == 3:
        return (mat[0][0] * (mat[1][1] * mat[2][2] - mat[1][2] * mat[2][1]) -
                mat[0][1] * (mat[1][0] * mat[2][2] - mat[1][2] * mat[2][0]) +
                mat[0][2] * (mat[1][0] * mat[2][1] - mat[1][1] * mat[2][0]))

    flag, tmp = False, 1

    for i in range(n):
        if not mat[i][i]:
            for j in range(i + 1, n):
                if mat[j][i]:
                    for k in range(i, n):
                        mat[j][k], mat[i][k] = mat[i][k], mat[j][k]
                    flag = not flag
                    break

        if not mat[i][i]:
            return 0

        for j in range(i + 1, n):
            if mat[j][i]:
                tmp = tmp * mat[i][i] if mod == 0 else tmp * mat[i][i] % mod
                t = mat[j][i]

                for k in range(i, n):
                    if mod == 0:
                        mat[j][k] = mat[j][k] * mat[i][i] - mat[i][k] * t
                    else:
                        mat[j][k] = (mat[j][k] * mat[i][i] - mat[i][k]) % mod

    res = pow(tmp, mod - 2, mod) if mod else 1

    for i in range(n):
        res = res * mat[i][i] % mod if mod else res * mat[i][i]
    if flag:
        return mod - res

    return res if mod else res // tmp


def inverse(mat):
    n = len(mat)
    determinant = det(mat)

    if n == 2:
        return [[mat[1][1] / determinant, -1 * mat[0][1] / determinant],
                [-1 * mat[1][0] / determinant, mat[0][0] / determinant]]

    return transpose([[(pow(-1, i + j) * det(minor(mat, i, j))) / determinant for j in range(n)] for i in range(n)])
