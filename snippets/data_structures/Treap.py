import random

left_child = [0]
right_child = [0]
_keys = [0]
_prior = [0.0]


def create_node(key):
    _keys.append(key)
    _prior.append(random.random())
    left_child.append(0)
    right_child.append(0)
    return len(_keys) - 1


def split(root, key):
    left_pos = right_pos = 0
    while root:
        if key < _keys[root]:
            left_child[right_pos] = right_pos = root
            root = left_child[root]
        else:
            right_child[left_pos] = left_pos = root
            root = right_child[root]
    left, right = right_child[0], left_child[0]
    right_child[left_pos] = left_child[right_pos] = right_child[0] = left_child[0] = 0
    return left, right


def merge(left, right):
    where, pos = left_child, 0
    while left and right:
        if _prior[left] > _prior[right]:
            where[pos] = pos = left
            where = right_child
            left = right_child[left]
        else:
            where[pos] = pos = right
            where = left_child
            right = left_child[right]
    where[pos] = left or right
    node = left_child[0]
    left_child[0] = 0
    return node


def insert(root, key):
    left, right = split(root, key)
    return merge(merge(left, create_node(key)), right)


def erase(root, key):
    if _keys[root] == key:
        return merge(left_child[root], right_child[root])
    node = root
    while _keys[root] != key:
        parent = root
        root = left_child[root] if key < _keys[root] else right_child[root]
    if root == left_child[parent]:
        left_child[parent] = merge(left_child[root], right_child[root])
    else:
        right_child[parent] = merge(left_child[root], right_child[root])
    return node


def ceiling_key(root, key):
    while root and _keys[root] < key:
        root = right_child[root]
    if not root:
        return 0
    min_node = root
    min_key = _keys[root]
    while root:
        if _keys[root] < key:
            root = right_child[root]
        else:
            if _keys[root] < min_key:
                min_key = _keys[root]
                min_node = root
            root = left_child[root]
    return min_node


def higher_key(root, key):
    while root and _keys[root] <= key:
        root = right_child[root]
    if not root:
        return 0
    min_node = root
    min_key = _keys[root]
    while root:
        if _keys[root] <= key:
            root = right_child[root]
        else:
            if _keys[root] < min_key:
                min_key = _keys[root]
                min_node = root
            root = left_child[root]
    return min_node


def floor_key(root, key):
    while root and _keys[root] > key:
        root = left_child[root]
    if not root:
        return 0
    max_node = root
    max_key = _keys[root]
    while root:
        if _keys[root] > key:
            root = left_child[root]
        else:
            if _keys[root] > max_key:
                max_key = _keys[root]
                max_node = root
            root = right_child[root]
    return max_node


def lower_key(root, key):
    while root and _keys[root] >= key:
        root = left_child[root]
    if not root:
        return 0
    max_node = root
    max_key = _keys[root]
    while root:
        if _keys[root] >= key:
            root = left_child[root]
        else:
            if _keys[root] > max_key:
                max_key = _keys[root]
                max_node = root
            root = right_child[root]
    return max_node


values = sorted([])
node_cnt = 1


def build(begin, end):
    global node_cnt
    if begin == end:
        return 0
    mid = (begin + end) // 2
    root = node_cnt
    node_cnt += 1
    _prior[root] = random.random()
    _keys[root] = values[mid]
    left_child[root] = build(begin, mid)
    right_child[root] = build(mid + 1, end)
    return root


class myset(object):
    def __init__(self):
        self.root = 0

    def insert(self, key):
        if not self.root:
            self.root = create_node(key)
        else:
            self.root = insert(self.root, key)

    def erase(self, key):
        self.root = erase(self.root, key)

    def ceiling_key(self, key):
        x = ceiling_key(self.root, key) if self.root else 0
        return _keys[x] if x else None

    def higher_key(self, key):
        x = higher_key(self.root, key) if self.root else 0
        return _keys[x] if x else None

    def floor_key(self, key):
        x = floor_key(self.root, key) if self.root else 0
        return _keys[x] if x else None

    def lower_key(self, key):
        x = lower_key(self.root, key) if self.root else 0
        return _keys[x] if x else None
