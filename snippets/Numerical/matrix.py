import operator as op

transpose = lambda mat: list(map(list, zip(*mat)))

minor = lambda mat, i, j: [row[:j] + row[j + 1:] for row in (mat[:i] + mat[i + 1:])]

mat_add = lambda *mat: [[sum(elements) for elements in zip(*row)] for row in zip(*mat)]

mat_sub = lambda A, B: [[i - j for i, j in zip(*row)] for row in zip(A, B)]

mat_mul = lambda A, B: list(map(lambda row: list(map(lambda *column: sum(map(op.mul, row, column)), *B)), A))

vec_mul = lambda vec, mat: [sum(vec_i * col[i] for i, vec_i in enumerate(vec)) for col in zip(*mat)]


def mat_mul_mod(A, B, mod):
    n, p = len(A), len(B[0])
    fmod = float(mod)

    B = [[(Bij & (2**16 - 1)) + 1j * (Bij >> 16) for Bij in Bi] for Bi in B]
    C = [[0] * p for _ in range(n)]

    for i, Ai in enumerate(A):
        row = [0.0] * p
        for j, Bj in enumerate(B):
            Aij = Ai[j] + 1j * ((Ai[j] << 16) % mod)
            for k, Bjk in enumerate(Bj):
                row[k] += Aij.real * Bjk.real + Aij.imag * Bjk.imag

        C[i] = [int(j % fmod) for j in row]

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
