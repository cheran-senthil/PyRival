import random

values = sorted()

MAXN = 2 * 10**5 + 1
left_child = [0] * MAXN
right_child = [0] * MAXN
keys = [0] * MAXN
priority = [0.0] * MAXN
cur = 1


def build(begin, end):
    global cur
    if begin == end:
        return 0
    mid = (begin + end) // 2
    root = cur
    cur += 1
    priority[root] = random.random()
    keys[root] = values[mid]
    left_child[root] = build(begin, mid)
    right_child[root] = build(mid + 1, end)
    return root


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


def erase(n, key):
    if keys[n] == key:
        return merge(left_child[n], right_child[n])
    m = n
    while keys[n] != key:
        parent = n
        n = left_child[n] if key < keys[n] else right_child[n]
    if n == left_child[parent]:
        left_child[parent] = merge(left_child[n], right_child[n])
    else:
        right_child[parent] = merge(left_child[n], right_child[n])
    return m


def lower_bound(n, key):
    while n and keys[n] < key:
        n = right_child[n]
    if not n:
        return 0
    best_node = n
    best = keys[n]
    while n:
        if keys[n] < key:
            n = right_child[n]
        else:
            if keys[n] < best:
                best = keys[n]
                best_node = n
            n = left_child[n]
    return best_node
