from itertools import imap, izip
from math import acos
from operator import mul

# line: ax + by + c = 0 is (a, b, c)

pointsToLine = lambda p1, p2: (p2[1] - p1[1], p1[0] - p2[0], p1[1]*p2[0] - p1[0]*p2[1])

areParallel = lambda l1, l2: l1[0] * l2[1] == l2[0] * l1[1]

toVec = lambda a, b: (i - j for i, j in izip(a, b))

dot = lambda A, B: sum(imap(mul, A, B))

norm_sq = lambda v: sum(i*i for i in v)

angle = lambda oa, ob: acos(dot(oa, ob) / (norm_sq(oa) * norm_sq(ob))**0.5)
