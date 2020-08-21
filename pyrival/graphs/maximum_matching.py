import itertools
from random import randint

_DEFAULT_PRIME = 1073750017


def maximum_matching(edges, mod=_DEFAULT_PRIME):
    """
    Returns the maximum cardinality matching of any simple graph (undirected, unweighted, no self-loops)
    Uses a randomized algorithm to compute the rank of the Tutte matrix
    The rank of the Tutte matrix is equal to twice the size of the maximum matching with high probability
    The probability for error is not more than n/mod

    Complexity: O(n ^ 3) worst case, O(n * |matching_size|) on average

    :param edges: a list of edges, assume nodes can be anything numbered from 0 to max number in edges
    :param mod: optional, a large random prime
    :return: the maximum cardinality matching of the graph
    """

    n = max(itertools.chain(*edges)) + 1
    matrix = _get_tutte_matrix(n, edges, mod)
    return _gauss(n, matrix, mod) // 2


def _get_tutte_matrix(n, edges, mod):
    matrix = [[0] * n for _ in range(n)]

    for u, v in edges:
        val = randint(1, mod - 1)
        matrix[u][v], matrix[v][u] = val, mod - val

    return matrix


def _gauss(n, matrix, mod):
    r = 0
    for j in range(n):
        k = r
        while k < n and not matrix[k][j]:
            k += 1

        if k == n:
            continue

        inv = pow(matrix[k][j], mod - 2, mod)
        for i in range(n):
            matrix[k][i] = inv * matrix[k][i] % mod
        matrix[k], matrix[r] = matrix[r], matrix[k]

        for u in range(r + 1, n):
            # reducing indexing costs to gain performance boost for the next loop
            matrix_u, matrix_r = matrix[u], matrix[r]
            if matrix_u[j]:
                for v in range(j + 1, n):
                    if matrix_r[v]:
                        matrix_u[v] = (matrix_u[v] - matrix_r[v] * matrix_u[j]) % mod

        r += 1

    return r
