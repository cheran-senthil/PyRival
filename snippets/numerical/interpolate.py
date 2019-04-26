def interpolate(points):
    n = len(points)
    x, y = map(list, zip(*points))
    for k in range(n - 1):
        for i in range(k + 1, n):
            y[i] = (y[i] - y[k]) / (x[i] - x[k])

    res, tmp = [0] * n, [0] * n
    tmp[0] = 1
    last = 0
    for k in range(n):
        for i in range(n):
            res[i] += y[k] * tmp[i]
            last, tmp[i] = tmp[i], last
            tmp[i] -= last * x[k]
    return res
