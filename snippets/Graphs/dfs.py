from collections import deque


def dfs(tree, start=0):
    stack = deque([start])
    out = []
    while stack:
        cur_node = stack.popleft()
        out.append(cur_node)
        stack.extendleft(tree[cur_node])
    return out
