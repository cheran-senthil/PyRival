import itertools
from random import randint


def maximum_matching(edges, mod=1073750017):
    n = max(itertools.chain(*edges)) + 1
    matrix = _get_tutte_matrix(n, edges, mod)
    return _get_matrix_rank(matrix, mod) // 2


def _get_tutte_matrix(n, edges, mod):
    matrix = [[0 for _ in range(n)] for _ in range(n)]

    for u, v in edges:
        i, j = min(u, v), max(u, v)
        v = randint(1, mod - 1)
        matrix[i][j], matrix[j][i] = v, mod - v

    return matrix


def _get_matrix_rank(matrix, mod):
    r, n = 0, len(matrix)
    for j in range(n):
        k = r
        while k < n and not matrix[k][j]:
            k += 1

        if k == n:
            continue

        inv = pow(matrix[k][j], mod - 2, mod)
        for i in range(n):
            x = matrix[k][i]
            matrix[k][i], matrix[r][i] = matrix[r][i], inv * x % mod

        for u in range(r + 1, n):
            if not matrix[u][j]:
                continue

            for v in range(j + 1, n):
                if matrix[r][v]:
                    matrix[u][v] = (matrix[u][v] - matrix[r][v] * matrix[u][j]) % mod
                    if matrix[u][v] < 0:
                        matrix[u][v] += mod

        r += 1

    return r
