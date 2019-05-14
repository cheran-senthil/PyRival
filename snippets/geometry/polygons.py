dist = lambda p1, p2: sum((a - b) * (a - b) for a, b in zip(p1, p2))**0.5

perimeter = lambda *p: sum(dist(i, j) for i, j in zip(p, p[1:] + p[:1]))

area = lambda *p: abs(sum(i[0] * j[1] - j[0] * i[1] for i, j in zip(p, p[1:] + p[:1]))) / 2

is_in_circle = lambda p, c, r: sum(i * i - j * j for i, j in zip(p, c)) < r * r

incircle_radius = lambda a, b, c: area(a, b, c) / (perimeter(a, b, c) / 2)

circumcircle_radius = lambda a, b, c: (dist(a, b) * dist(b, c) * dist(c, a)) / (4 * area(a, b, c))
