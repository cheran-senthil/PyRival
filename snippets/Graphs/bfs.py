from collections import deque


def bfs(tree, start=0):
    queue = deque([start])
    out = []
    while queue:
        cur_node = queue.popleft()
        out.append(cur_node)
        queue.extend(tree[cur_node])
    return out


def bfs_depth(tree, start=0):
    q, ret = [start], []
    while q:
        ret.append(q)
        q = [i for node in q for i in tree[node]]
    return ret
