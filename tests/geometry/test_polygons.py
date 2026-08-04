from pyrival.geometry.polygons import is_in_circle


def test_is_in_circle_with_nonzero_center():
    assert is_in_circle((11, 10), (10, 10), 2)
    assert not is_in_circle((13, 10), (10, 10), 2)
