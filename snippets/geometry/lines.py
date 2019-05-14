import itertools
import math
from math import gcd

# 2d line: ax + by + c = 0  is  (a, b, c)

#          ax + by + c = 0     ((a, b, c),
# 3d line: dx + ez + f = 0  is  (d, e, f),
#          gy + hz + i = 0      (g, h, i))


def get_2dline(p1, p2):
    if p1 == p2:
        return (0, 0, 0)
    _p1, _p2 = min(p1, p2), max(p1, p2)
    a, b, c = _p2[1] - _p1[1], _p1[0] - _p2[0], _p1[1] * _p2[0] - _p1[0] * _p2[1]
    g = gcd(gcd(a, b), c)
    return (a // g, b // g, c // g)


dist = lambda p1, p2: sum((a - b) * (a - b) for a, b in zip(p1, p2))**0.5

get_line = lambda p1, p2: map(get_2dline, itertools.combinations(p1, 2), itertools.combinations(p2, 2))

is_parallel = lambda l1, l2: l1[0] * l2[1] == l2[0] * l1[1]

is_same = lambda l1, l2: is_parallel(l1, l2) and (l1[1] * l2[2] == l2[1] * l1[2])

collinear = lambda p1, p2, p3: is_same(get_2dline(p1, p2), get_2dline(p2, p3))

intersect = lambda l1, l2: None if is_parallel(l1, l2) else ((l2[1] * l1[2] - l1[1] * l2[2]) / (l2[0] * l1[1] - l1[
    0] * l2[1]), (l1[0] * l2[2] - l1[2] * l2[0]) / (l2[0] * l1[1] - l1[0] * l2[1]))

rotate = lambda p, theta, origin=(0, 0): (origin[0] + (p[0] - origin[0]) * math.cos(theta) - (p[1] - origin[
    1]) * math.sin(theta), origin[1] + (p[0] - origin[0]) * math.sin(theta) + (p[1] - origin[1]) * math.cos(theta))
