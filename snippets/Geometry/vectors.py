from math import acos
from operator import mul

# oa = toVec(o, a), ob = toVec(o, b)

toVec = lambda p1, p2: (i - j for i, j in zip(p1, p2))


scale = lambda v, s: (i*s for i in v)


translate = lambda p, v: (pi + vi for pi, vi in zip(p, v))


dot = lambda v1, v2: sum(map(mul, v1, v2))


norm_sq = lambda v: sum(i*i for i in v)


angle = lambda oa, ob: acos(dot(oa, ob) / (norm_sq(oa) * norm_sq(ob))**0.5)


projection = lambda a, b, c: dot(toVec(a, c), toVec(a, b)) / norm_sq(toVec(a, b))


lineDistance = lambda p, a, b: translate(a, dot(toVec(a, p), toVec(a, b)) / norm_sq(toVec(a, b)))


segmentDistance = lambda p, a, b: a if projection(a, b, p) < 0 else b if projection(a, b, p) > 1 else lineDistance(p, a, b)


cross2d = lambda v1, v2: v1[0] * v2[1] - v1[1] * v2[0]


cross3d = lambda v1, v2: (v1[1] * v2[2] - v1[2] * v2[1],
                          v1[2] * v2[0] - v1[0] * v2[2],
                          v1[0] * v2[1] - v1[1] * v2[0])
