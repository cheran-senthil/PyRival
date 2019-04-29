import random

values = sorted()

MX = 2 * 10**5 + 10
lt = [0] * MX
rt = [0] * MX
k = [0] * MX
pr = [0.0] * MX
cur = 1


def build(i, j):
    global cur
    if i == j:
        return 0
    mid = (i + j) // 2
    root = cur
    cur += 1
    pr[root] = random.random()
    k[root] = values[mid]
    lt[root] = build(i, mid)
    rt[root] = build(mid + 1, j)
    return root


def merge(left, right):
    tmp = [0]
    where, pos = tmp, 0
    while left and right:
        if pr[left] > pr[right]:
            where[pos] = left
            where, pos = rt, left
            left = rt[left]
        else:
            where[pos] = right
            where, pos = lt, right
            right = lt[right]
    where[pos] = left or right
    return tmp[0]


def erase(n, key):
    if k[n] == key:
        return merge(lt[n], rt[n])
    m = n
    while k[n] != key:
        if key < k[n]:
            parent = n
            n = lt[n]
        else:
            parent = n
            n = rt[n]
    if n == lt[parent]:
        lt[parent] = merge(lt[n], rt[n])
    else:
        rt[parent] = merge(lt[n], rt[n])
    return m


def lower_bound(n, key):
    while n and k[n] < key:
        n = rt[n]
    if not n:
        return 0
    best_node = n
    best = k[n]
    while n:
        if k[n] < key:
            n = rt[n]
        else:
            if k[n] < best:
                best = k[n]
                best_node = n
            n = lt[n]
    return best_node
