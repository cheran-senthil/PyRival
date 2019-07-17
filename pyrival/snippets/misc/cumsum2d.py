def cumsum2d(A):  # Input 2D square int matrix N x N
    n = len(A)
    p = [[0] * (n + 1) for _ in range(n + 1)]
    for i, Ai in enumerate(A):
        pi, pii = p[i], p[i + 1]
        for j, Aij in enumerate(Ai):
            pii[j + 1] = Ai[j] + pi[j + 1] + pii[j] - pi[j]

    return lambda a, b, x, y: p[x][y] - p[x][b] - p[a][y] + p[a][b]
