from pyrival.data_structures.LinkedList import LinkedList


def test_iterable_constructor():
    linked_list = LinkedList([1, 2, 3])
    assert linked_list.to_list() == [1, 2, 3]
    assert len(linked_list) == 3
