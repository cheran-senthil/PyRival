MOD = 10**9 + 7

MAGIC = 6755399441055744.0
MODF = float(MOD)
SHRT = 65536.0

MODF_INV = 1.0 / MODF
SHRT_INV = 1.0 / SHRT

fround = lambda x: (x + MAGIC) - MAGIC
fmod = lambda a: a - MODF * fround(MODF_INV * a)
fmul = lambda a, b, c=0.0: fmod(fmod(a * SHRT) * fround(SHRT_INV * b) + a * (b - SHRT * fround(b * SHRT_INV)) + c)


def fpow(x, y):
    if y == 0:
        return 1.0

    res = 1.0
    while y > 1:
        if y & 1 == 1:
            res = fmul(res, x)
        x = fmul(x, x)
        y >>= 1

    return fmul(res, x)


transpose = lambda mat: [list(col) for col in zip(*mat)]

minor = lambda mat, i, j: [row[:j] + row[j + 1:] for row in (mat[:i] + mat[i + 1:])]

mat_add = lambda *mat: [[sum(elements) for elements in zip(*row)] for row in zip(*mat)]

mat_sub = lambda A, B: [[i - j for i, j in zip(*row)] for row in zip(A, B)]

mat_mul = lambda A, B: [[sum(i * j for i, j in zip(row, col)) for col in zip(*B)] for row in A]

vec_mul = lambda mat, vec: [sum(a * b for a, b in zip(row, vec)) for row in mat]


def mat_mul_mod(A, B):
    C = [[0.0] * len(B[0]) for _ in range(len(A))]
    for i, A_i in enumerate(A):
        C_i = C[i]
        for j, B_j in enumerate(B):
            Aij = A_i[j]
            for k, Bjk in enumerate(B_j):
                C_i[k] = fmul(Bjk, Aij, C_i[k])
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

    while power > 1:
        if power & 1 == 1:
            result = mat_mul(result, mat)
        mat = mat_mul(mat, mat)
        power >>= 1

    return mat_mul(result, mat)


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
                tmp = fmul(tmp, mat[i][i]) if mod else tmp * mat[i][i]
                t = mat[j][i]

                for k in range(i, n):
                    if mod == 0:
                        mat[j][k] = mat[j][k] * mat[i][i] - mat[i][k] * t
                    else:
                        mat[j][k] = fmul(mat[j][k], mat[i][i], -mat[i][k])

    res = fpow(tmp, mod - 2) if mod else 1

    for i in range(n):
        res = fmul(res, mat[i][i]) if mod else res * mat[i][i]
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
