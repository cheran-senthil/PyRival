from __future__ import division

from bisect import bisect_left


def convex_hull_trick(K, M, integer=True):
    """
    Given lines on the form y = K[i] * x + M[i] this function returns intervals,
    such that on each interval the convex hull is made up of a single line.
    Input:
        K: list of the slopes
        M: list of the constants (value at x = 0)
        interger: boolean for turning on / off integer mode. Integer mode is exact, it
                  works by effectively flooring the seperators of the intervals.
    Return:
        hull_i: on interval j, line i = hull_i[j] is >= all other lines
        hull_x: interval j and j + 1 is separated by x = hull_x[j], (hull_x[j] is the last x in interval j)
    """
    if integer:
        intersect = lambda i, j: (M[j] - M[i]) // (K[i] - K[j])
    else:
        intersect = lambda i, j: (M[j] - M[i]) / (K[i] - K[j])

    # assert len(K) == len(M)

    hull_i = []
    hull_x = []
    order = sorted(range(len(K)), key=K.__getitem__)
    for i in order:
        while True:
            if not hull_i:
                hull_i.append(i)
                break
            elif K[hull_i[-1]] == K[i]:
                if M[hull_i[-1]] >= M[i]:
                    break
                hull_i.pop()
                if hull_x: hull_x.pop()
            else:
                x = intersect(i, hull_i[-1])
                if hull_x and x <= hull_x[-1]:
                    hull_i.pop()
                    hull_x.pop()
                else:
                    hull_i.append(i)
                    hull_x.append(x)
                    break
    return hull_i, hull_x


def max_query(x, K, M, hull_i, hull_x):
    """ Find maximum value at x in O(log n) time """
    i = hull_i[bisect_left(hull_x, x)]
    return K[i] * x + M[i]
