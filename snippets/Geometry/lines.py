from math import acos
from operator import mul
from itertools import combinations

# 2d line: ax + by + c = 0  is  (a, b, c)

# 3d line: ax + by + c = 0     ((a, b, c),
#          dx + ez + f = 0  is  (d, e, f),
#          gy + hz + i = 0      (g, h, i))

pointsToLine2d = lambda p1, p2: (p2[1] - p1[1], p1[0] - p2[0], p1[1]*p2[0] - p1[0]*p2[1])

pointsToLine = lambda p1, p2: map(pointsToLine2d, combinations(p1, 2), combinations(p2, 2))

areParallel = lambda l1, l2: l1[0] * l2[1] == l2[0] * l1[1]

toVec = lambda a, b: (i - j for i, j in zip(a, b))

dot = lambda A, B: sum(map(mul, A, B))

norm_sq = lambda v: sum(i*i for i in v)

angle = lambda oa, ob: acos(dot(oa, ob) / (norm_sq(oa) * norm_sq(ob))**0.5)
