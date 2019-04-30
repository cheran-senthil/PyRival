import random

left_child = [0]
right_child = [0]
keys = [0]
priority = [0]


def create_node(key):
    keys.append(key)
    priority.append(random.random())
    left_child.append(0)
    right_child.append(0)
    return len(keys) - 1


def split(root, key):
    tmp = [0, 0]
    wherel, wherer, posl, posr = tmp, tmp, 0, 1
    while root:
        if key < keys[root]:
            wherer[posr] = root
            wherer, posr = left_child, root
            root = left_child[root]
        else:
            wherel[posl] = root
            wherel, posl = right_child, root
            root = right_child[root]
    wherel[posl] = wherer[posr] = 0
    return tmp


def insert(root, key):
    left, right = split(root, key)
    return merge(merge(left, create_node(key)), right)


def merge(left, right):
    tmp = [0]
    where, pos = tmp, 0
    while left and right:
        if priority[left] > priority[right]:
            where[pos] = left
            where, pos = right_child, left
            left = right_child[left]
        else:
            where[pos] = right
            where, pos = left_child, right
            right = left_child[right]
    where[pos] = left or right
    return tmp[0]


def erase(root, key):
    if keys[root] == key:
        return merge(left_child[root], right_child[root])
    node = root
    while keys[root] != key:
        parent = root
        root = left_child[root] if key < keys[root] else right_child[root]
    if root == left_child[parent]:
        left_child[parent] = merge(left_child[root], right_child[root])
    else:
        right_child[parent] = merge(left_child[root], right_child[root])
    return node


def lower_bound(root, key):
    while root and keys[root] < key:
        root = right_child[root]
    if not root:
        return 0
    max_node = root
    max_key = keys[root]
    while root:
        if keys[root] < key:
            root = right_child[root]
        else:
            if keys[root] < max_key:
                max_key = keys[root]
                max_node = root
            root = left_child[root]
    return max_node


values = sorted()


def build(begin, end):
    global node_cnt
    if begin == end:
        return 0
    mid = (begin + end) // 2
    root = node_cnt
    node_cnt += 1
    priority[root] = random.random()
    keys[root] = values[mid]
    left_child[root] = build(begin, mid)
    right_child[root] = build(mid + 1, end)
    return root
