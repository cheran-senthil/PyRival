dist = lambda p1, p2: sum((a - b)*(a - b) for a, b in zip(p1, p2))**0.5


perimeter = lambda p: sum(dist(p[i], p[i + 1]) for i in range(len(p) - 1))


area = lambda p: abs(sum(i[0] * j[1] - j[0] * i[1] for i, j in zip(p, p[1:] + p[0]))) / 2


insideCircle = lambda p, c, r: sum(i*i - j*j for i, j in zip(p, c)) < r*r


rInCircle = lambda a, b, c: area(dist(a, b), dist(b, c), dist(c, a)) / (perimeter(dist(a, b), dist(b, c), dist(c, a)) / 2)
