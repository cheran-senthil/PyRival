from collections import deque


def bfs(tree, start=0):
    queue = deque([start])
    out = []
    while queue:
        cur_node = queue.popleft()
        out.append(cur_node)
        queue.extend(tree[cur_node])
    return out
