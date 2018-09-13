from math import acos
from operator import mul

# oa = toVec(o, a), ob = toVec(o, b)

toVec = lambda p1, p2: (i - j for i, j in zip(p1, p2))


scale = lambda v, s: (i*s for i in v)


translate = lambda p, v: (pi + vi for pi, vi in zip(p, v))


dot = lambda v1, v2: sum(map(mul, v1, v2))


norm_sq = lambda v: sum(i*i for i in v)


angle = lambda oa, ob: acos(dot(oa, ob) / (norm_sq(oa) * norm_sq(ob))**0.5)
