from pyrival.phi import phi as f


def test_phi(phi):
    assert f(len(phi) - 1) == phi
