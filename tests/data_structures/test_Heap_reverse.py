from pyrival.data_structures.Heap import Heap


def test_reverse_heap():
    heap = Heap([1, 3, 2], reverse=True)
    assert [heap.pop(), heap.pop(), heap.pop()] == [3, 2, 1]
