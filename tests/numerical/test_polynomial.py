from pyrival.numerical.polynomial import divroot


def test_divroot():
    assert divroot([-2, 1, 1], 1) == [2, 1]
