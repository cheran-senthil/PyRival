from pyrival.data_structures.Heap import Heap


def test_heap_repr():
    assert repr(Heap([2, 1])) == "Heap([1, 2])"
