from pyrival.geometry.lines import is_same


def test_distinct_vertical_lines_are_not_same():
    assert not is_same((1, 0, 0), (1, 0, -1))
    assert is_same((1, 0, -1), (2, 0, -2))
