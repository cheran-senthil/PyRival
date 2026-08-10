import random

from pyrival.data_structures.Heap import RemovalHeap


def test_duplicates():
    heap = RemovalHeap([3, 1, 1, 2])
    heap.remove(1)

    assert len(heap) == 3
    assert [heap.pop(), heap.pop(), heap.pop()] == [1, 2, 3]


def test_unhashable_values():
    heap = RemovalHeap([[2], [1], [1]])
    heap.remove([1])

    assert list(heap) == [[1], [2]]


def test_update():
    heap = RemovalHeap([(5, "a"), (2, "b")])
    heap.update((5, "a"), (1, "a"))

    assert heap.peek() == (1, "a")
    assert list(heap) == [(1, "a"), (2, "b")]


def test_pushpop_and_poppush():
    heap = RemovalHeap([2, 3])

    assert heap.pushpop(1) == 1
    assert heap.pushpop(4) == 2
    assert heap.poppush(5) == 3
    assert list(heap) == [4, 5]


def test_random_operations():
    rng = random.Random(0)
    heap = RemovalHeap()
    values = []

    for _ in range(1000):
        operation = rng.randrange(4) if values else 0
        if operation == 0:
            value = rng.randrange(20)
            heap.push(value)
            values.append(value)
        elif operation == 1:
            index = rng.randrange(len(values))
            heap.remove(values.pop(index))
        elif operation == 2:
            index = rng.randrange(len(values))
            old, new = values[index], rng.randrange(20)
            heap.update(old, new)
            values[index] = new
        else:
            value = min(values)
            values.remove(value)
            assert heap.pop() == value

        assert len(heap) == len(values)
        assert list(heap) == sorted(values)
        if values:
            assert heap.peek() == min(values)
