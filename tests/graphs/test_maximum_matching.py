from pyrival.maximum_matching import *


def test_maximum_matching__corner_cases():
    edges = []
    for e in [(0, 1), (1, 2), (2, 0)]:
        edges.append(e)
        assert maximum_matching(edges) == 1

    for e in [(2, 3), (3, 4)]:
        edges.append(e)
        assert maximum_matching(edges) == 2

    for e in [(4, 5), (5, 6)]:
        edges.append(e)
        assert maximum_matching(edges) == 3

    for e in [(7, 8), (7, 9), (7, 10)]:
        edges.append(e)
        assert maximum_matching(edges) == 4

    edges.append((4, 10))
    assert maximum_matching(edges) == 5

    for e in [(9, 11), (8, 11)]:
        edges.append(e)
        assert maximum_matching(edges) == 6


def test_maximum_matching__large_pseudorandom_cases():
    n = 500
    edges = []
    for i in range(n):
        for k in range(13):
            j = (i * i + k * 79 + abs(i * i - k)) % n
            if i != j:
                edges.append((i, j))

    assert maximum_matching(edges) == 239
