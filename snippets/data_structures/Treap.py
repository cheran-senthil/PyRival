import random


class TreapMultiSet(object):
    root = 0
    size = 0

    def __init__(self, data=None):
        if data:
            data = sorted(data)
            self.root = treap_builder(data)
            self.size = len(data)

    def add(self, key):
        self.root = treap_insert(self.root, key)
        self.size += 1

    def remove(self, key):
        self.root = treap_erase(self.root, key)
        self.size -= 1

    def discard(self, key):
        try:
            self.remove(key)
        except KeyError:
            pass

    def ceiling(self, key):
        x = treap_ceiling(self.root, key)
        return treap_keys[x] if x else None

    def higher(self, key):
        x = treap_higher(self.root, key)
        return treap_keys[x] if x else None

    def floor(self, key):
        x = treap_floor(self.root, key)
        return treap_keys[x] if x else None

    def lower(self, key):
        x = treap_lower(self.root, key)
        return treap_keys[x] if x else None

    def max(self):
        return treap_keys[treap_max(self.root)]

    def min(self):
        return treap_keys[treap_min(self.root)]

    def __len__(self):
        return self.size

    def __nonzero__(self):
        return bool(self.root)

    __bool__ = __nonzero__

    def __contains__(self, key):
        return self.floor(key) == key

    def __repr__(self):
        return 'TreapMultiSet({})'.format(list(self))

    def __iter__(self):
        if not self.root:
            return iter([])
        out = []
        stack = [self.root]
        while stack:
            node = stack.pop()
            if node > 0:
                if right_child[node]:
                    stack.append(right_child[node])
                stack.append(~node)
                if left_child[node]:
                    stack.append(left_child[node])
            else:
                out.append(treap_keys[~node])
        return iter(out)


class TreapSet(TreapMultiSet):
    def add(self, key):
        self.root, duplicate = treap_insert_unique(self.root, key)
        if not duplicate:
            self.size += 1

    def __repr__(self):
        return 'TreapSet({})'.format(list(self))


class TreapHashSet(TreapMultiSet):
    def __init__(self, data=None):
        if data:
            self.keys = set(data)
            super(TreapHashSet, self).__init__(self.keys)
        else:
            self.keys = set()

    def add(self, key):
        if key not in self.keys:
            self.keys.add(key)
            super(TreapHashSet, self).add(key)

    def remove(self, key):
        self.keys.remove(key)
        super(TreapHashSet, self).remove(key)

    def discard(self, key):
        if key in self.keys:
            self.remove(key)

    def __contains__(self, key):
        return key in self.keys

    def __repr__(self):
        return 'TreapHashSet({})'.format(list(self))


class TreapHashMap(TreapMultiSet):
    def __init__(self, data=None):
        if data:
            self.map = dict(data)
            super(TreapHashMap, self).__init__(self.map.keys())
        else:
            self.map = dict()

    def __setitem__(self, key, value):
        if key not in self.map:
            super(TreapHashMap, self).add(key)
        self.map[key] = value

    def __getitem__(self, key):
        return self.map[key]

    def add(self, key):
        raise TypeError("add on TreapHashMap")

    def get(self, key, default=None):
        return self.map.get(key, default=default)

    def remove(self, key):
        self.map.pop(key)
        super(TreapHashMap, self).remove(key)

    def discard(self, key):
        if key in self.map:
            self.remove(key)

    def __contains__(self, key):
        return key in self.map

    def __repr__(self):
        return 'TreapHashMap({})'.format(list(self))


left_child = [0]
right_child = [0]
treap_keys = [0]
treap_prior = [0.0]


def treap_builder(sorted_data):
    """Build a treap in O(n) time using sorted data"""

    def build(begin, end):
        if begin == end:
            return 0
        mid = (begin + end) // 2
        root = treap_create_node(sorted_data[mid])
        left_child[root] = build(begin, mid)
        right_child[root] = build(mid + 1, end)

        # sift down the priorities
        ind = root
        while True:
            lc = left_child[ind]
            rc = right_child[ind]

            if lc and treap_prior[lc] > treap_prior[ind]:
                if rc and treap_prior[rc] > treap_prior[rc]:
                    treap_prior[ind], treap_prior[rc] = treap_prior[rc], treap_prior[ind]
                    ind = rc
                else:
                    treap_prior[ind], treap_prior[lc] = treap_prior[lc], treap_prior[ind]
                    ind = lc
            elif rc and treap_prior[rc] > treap_prior[ind]:
                treap_prior[ind], treap_prior[rc] = treap_prior[rc], treap_prior[ind]
                ind = rc
            else:
                break
        return root

    return build(0, len(sorted_data))


def treap_create_node(key):
    treap_keys.append(key)
    treap_prior.append(random.random())
    left_child.append(0)
    right_child.append(0)
    return len(treap_keys) - 1


def treap_split(root, key):
    left_pos = right_pos = 0
    while root:
        if key < treap_keys[root]:
            left_child[right_pos] = right_pos = root
            root = left_child[root]
        else:
            right_child[left_pos] = left_pos = root
            root = right_child[root]
    left, right = right_child[0], left_child[0]
    right_child[left_pos] = left_child[right_pos] = right_child[0] = left_child[0] = 0
    return left, right


def treap_merge(left, right):
    where, pos = left_child, 0
    while left and right:
        if treap_prior[left] > treap_prior[right]:
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


def treap_insert(root, key):
    if not root:
        return treap_create_node(key)
    left, right = treap_split(root, key)
    return treap_merge(treap_merge(left, treap_create_node(key)), right)


def treap_insert_unique(root, key):
    if not root:
        return treap_create_node(key), False
    left, right = treap_split(root, key)
    if left and treap_keys[left] == key:
        return treap_merge(left, right), True
    return treap_merge(treap_merge(left, treap_create_node(key)), right), False


def treap_erase(root, key):
    if not root:
        raise KeyError(key)
    if treap_keys[root] == key:
        return treap_merge(left_child[root], right_child[root])
    node = root
    while root and treap_keys[root] != key:
        parent = root
        root = left_child[root] if key < treap_keys[root] else right_child[root]
    if not root:
        raise KeyError(key)
    if root == left_child[parent]:
        left_child[parent] = treap_merge(left_child[root], right_child[root])
    else:
        right_child[parent] = treap_merge(left_child[root], right_child[root])

    return node


def treap_ceiling(root, key):
    while root and treap_keys[root] < key:
        root = right_child[root]
    if not root:
        return 0
    min_node = root
    min_key = treap_keys[root]
    while root:
        if treap_keys[root] < key:
            root = right_child[root]
        else:
            if treap_keys[root] < min_key:
                min_key = treap_keys[root]
                min_node = root
            root = left_child[root]
    return min_node


def treap_higher(root, key):
    while root and treap_keys[root] <= key:
        root = right_child[root]
    if not root:
        return 0
    min_node = root
    min_key = treap_keys[root]
    while root:
        if treap_keys[root] <= key:
            root = right_child[root]
        else:
            if treap_keys[root] < min_key:
                min_key = treap_keys[root]
                min_node = root
            root = left_child[root]
    return min_node


def treap_floor(root, key):
    while root and treap_keys[root] > key:
        root = left_child[root]
    if not root:
        return 0
    max_node = root
    max_key = treap_keys[root]
    while root:
        if treap_keys[root] > key:
            root = left_child[root]
        else:
            if treap_keys[root] > max_key:
                max_key = treap_keys[root]
                max_node = root
            root = right_child[root]
    return max_node


def treap_lower(root, key):
    while root and treap_keys[root] >= key:
        root = left_child[root]
    if not root:
        return 0
    max_node = root
    max_key = treap_keys[root]
    while root:
        if treap_keys[root] >= key:
            root = left_child[root]
        else:
            if treap_keys[root] > max_key:
                max_key = treap_keys[root]
                max_node = root
            root = right_child[root]
    return max_node


def treap_min(root):
    if not root:
        raise ValueError('min on empty treap')
    while left_child[root]:
        root = left_child[root]
    return root


def treap_max(root):
    if not root:
        raise ValueError('max on empty treap')
    while right_child[root]:
        root = right_child[root]
    return root
