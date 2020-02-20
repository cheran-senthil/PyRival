import pyrival.algebra


def test_phi(phi):
    assert pyrival.algebra.phi(len(phi) - 1) == phi
