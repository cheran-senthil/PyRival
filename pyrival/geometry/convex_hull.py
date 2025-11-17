"""
    Given a list P of n points in 2D, convex_hull computes its convex hull in O(n log n) time.
    The points are returned clock-wise starting with the left-most upper-most point (i.e. min(P)).
"""

def convex_hull(P):
    P = sorted(P)
    cross = lambda a,b,c: (a[0] - b[0]) * (c[1] - b[1]) - (a[1] - b[1]) * (c[0] - b[0])
    H = []
    for p in P + P[::-1]:
        while len(H) > 1 and cross(H[-2], H[-1], p) <= 0 and not H[-2] < H[-1] > p:
            H.pop()
        H.append(p)
    return H[:-1]
