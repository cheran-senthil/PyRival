from pyrival.combinatorics import *

def test_catalan_recursive(A):
    assert all(catalan_recursive(i) == j for i, j in enumerate(A))


def test_derangements(A):
    assert all(derangements(i) == j for i, j in enumerate(A))


def test_catalan(A)
    assert all(catalan(i) == j for i, j in enumerate(A))
