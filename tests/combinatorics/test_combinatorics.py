from pyrival.combinatorics import combinatorics


def test_catalan_recursive(catalan):
    assert all(combinatorics.catalan_recursive(i) == j for i, j in enumerate(catalan))


def test_derangements(derangements):
    assert all(combinatorics.derangements(i) == j for i, j in enumerate(derangements))


def test_catalan(catalan):
    assert all(combinatorics.catalan(i) == j for i, j in enumerate(catalan))
