from pyrival.algebra.fst import fst_conv


def test_fst_conv():
    assert fst_conv([1, 2], [3, 4]) == [13, 8]
