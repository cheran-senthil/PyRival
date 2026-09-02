from pyrival.numerical.integrate import fast_quad


def test_fast_quad():
    assert abs(fast_quad(lambda x: x * x, 0, 1) - 1 / 3) < 1e-6
