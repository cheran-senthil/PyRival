import pyrival.combinatorics


def test_catalan_recursive(catalan):
    assert all(pyrival.combinatorics.catalan_recursive(i) == j for i, j in enumerate(catalan))


def test_derangements(derangements):
    assert all(pyrival.combinatorics.derangements(i) == j for i, j in enumerate(derangements))


def test_catalan(catalan):
    assert all(pyrival.combinatorics.catalan(i) == j for i, j in enumerate(catalan))
