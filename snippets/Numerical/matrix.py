import operator as op

transpose = lambda mat: list(map(list, zip(*mat)))

minor = lambda mat, i, j: [row[:j] + row[j + 1:] for row in (mat[:i]+mat[i + 1:])]

mat_add = lambda *mat: [[sum(elements) for elements in zip(*row)] for row in zip(*mat)]

mat_sub = lambda mat1, mat2: [[i - j for i, j in zip(*row)] for row in zip(mat1, mat2)]

mat_mul = lambda mat1, mat2: list(map(lambda row: list(map(lambda *column: sum(map(op.mul, row, column)), *mat2)), mat1))


def eye(m):
    identity = [[0]*m for _ in range(m)]
    for i, row in enumerate(identity):
        row[i] = 1

    return identity


def mat_pow(mat, power):
    if power < 0:
        return mat_pow(inverse(mat), -power)

    result = eye(len(mat))

    if power == 0:
        return result

    for i in '{0:b}'.format(power)[::-1]:
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


def inverse(m):
    determinant = det(m)
    if len(m) == 2:
        return [[m[1][1] / determinant, -1 * m[0][1] / determinant],
                [-1 * m[1][0] / determinant, m[0][0] / determinant]]

    return transpose([[(pow(-1, i + j) * det(minor(m, i, j))) / determinant for j in range(len(m))] for i in range(len(m))])


linear_recurrence = lambda trans_matrix, known_values, k: mat_mul(mat_pow(trans_matrix, k), known_values)
