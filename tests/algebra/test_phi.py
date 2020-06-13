from pyrival.phi import *

def test_phi(f):
    assert phi(len(f) - 1) == f
