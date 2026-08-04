from pyrival.data_structures.tree_repr import tree_repr


class Tree:
    _size = 2
    data = [None, 1, 2, 3]


def test_tree_repr():
    assert tree_repr(Tree()) == "  1  \n _^_ \n/   \\\n2   3"
