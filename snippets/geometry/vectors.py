import math

# oa = to_vec(o, a), ob = to_vec(o, b)

to_vec = lambda p1, p2: (j - i for i, j in zip(p1, p2))

scale = lambda v, s: (i * s for i in v)

translate = lambda p, v: (pi + vi for pi, vi in zip(p, v))

dot = lambda v1, v2: sum(i * j for i, j in zip(v1, v2))

norm_sq = lambda v: sum(i * i for i in v)

angle = lambda oa, ob: math.acos(dot(oa, ob) / (norm_sq(oa) * norm_sq(ob))**0.5)

cross2d = lambda v1, v2: v1[0] * v2[1] - v1[1] * v2[0]

cross3d = lambda v1, v2: (v1[1] * v2[2] - v1[2] * v2[1], v1[2] * v2[0] - v1[0] * v2[2], v1[0] * v2[1] - v1[1] * v2[0])


def closest_point(p, a, b, segment=False):
    ap, ab = to_vec(a, p), to_vec(a, b)

    u = dot(ap, ab) / norm_sq(ab)

    if segment:
        if u < 0:
            return a
        if u > 1:
            return b

    return translate(a, scale(ab, u))
