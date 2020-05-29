import itertools
from random import randint


_DEFAULT_PRIME = 1073750017


def maximum_matching(edges, mod=_DEFAULT_PRIME):
    """
    Returns the maximum cardinality matching of an undirected general graph
    Uses a randomized algorithm to compute the rank of the Tutte matrix
    The rank of the Tutte matrix is equal to twice the size of the maximum matching with high probability

    Complexity: O(n ^ 3) worst case, O(n * m) with high constant factor on average

    :param edges: a list of edges, assume nodes can be anything numbered from 0 to max number in edges
    :param mod: a large random prime
    :return: the maximum cardinality matching of the graph
    """

    edges = [(u, v) for u, v in edges if u != v]

    if not edges:
        return 0

    n = max(itertools.chain(*edges)) + 1
    matrix = _get_tutte_matrix(n, edges, mod)
    return _gauss(matrix, mod) // 2


def _get_tutte_matrix(n, edges, mod):
    matrix = [[0] * n for _ in range(n)]

    for u, v in edges:
        val = randint(1, mod - 1)
        matrix[u][v], matrix[v][u] = val, mod - val

    return matrix


def _gauss(matrix, mod):
    r, n = 0, len(matrix)
    for j in range(n):
        k = r
        while k < n and not matrix[k][j]:
            k += 1

        if k == n:
            continue

        inv = pow(matrix[k][j], mod - 2, mod)
        for i in range(n):
            matrix[k][i], matrix[r][i] = matrix[r][i], inv * matrix[k][i] % mod

        for u in range(r + 1, n):
            if not matrix[u][j]:
                continue

            for v in range(j + 1, n):
                if matrix[r][v]:
                    matrix[u][v] = (matrix[u][v] - matrix[r][v] * matrix[u][j]) % mod

        r += 1

    return r
