import random

values = sorted()


class Node:
    def __init__(self, key=0):
        self.left, self.right = None, None
        self.key = key
        self.priority = random.random()


def build(i, j):
    if i == j:
        return None
    mid = (i + j) // 2
    root = Node(values[mid])
    root.left = build(i, mid)
    root.right = build(mid + 1, j)
    return root


def merge(left, right):
    if not left or not right:
        return left if left else right
    if left.priority > right.priority:
        left.right = merge(left.right, right)
        return left
    right.left = merge(left, right.left)
    return right


def erase(node, key):
    if node is None:
        return None
    if key == node.key:
        return merge(node.left, node.right)
    elif key < node.key:
        node.left = erase(node.left, key)
    else:
        node.right = erase(node.right, key)
    return node


def lower_bound(n, key):
    if n is None:
        return None
    if key > n.key:
        return lower_bound(n.right, key)
    if key < n.key:
        ret = lower_bound(n.left, key)
        if ret and ret.key >= key:
            return ret
    return n
