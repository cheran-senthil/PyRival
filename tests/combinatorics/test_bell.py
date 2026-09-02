from pyrival.combinatorics.combinatorics import bell


def test_bell():
    assert [bell(n) for n in range(7)] == [1, 1, 2, 5, 15, 52, 203]
