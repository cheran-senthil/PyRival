def scc(graph):
    """
    Finds what strongly connected components each node
    is a part of in a directed graph,
    it also finds a weak topological ordering of the nodes
    """
    n = len(graph)
    comp = [-1] * n
    top_order = []

    Q = []
    stack = []
    new_node = None
    for root in range(n):
        if comp[root] >= 0:
            continue

        # Do a dfs while keeping track of depth
        Q.append(root)
        root_depth = len(top_order)
        while Q:
            node = Q.pop()
            if node >= 0:
                if comp[node] >= 0:
                    continue
                # First time

                # Index the node
                comp[node] = len(top_order) + len(stack)
                stack.append(node)

                # Do a dfs
                Q.append(~node)
                Q += graph[node]
            else:
                # Second time
                node = ~node

                # calc low link
                low = index = comp[node]
                for nei in graph[node]:
                    if root_depth <= comp[nei]:
                        low = min(low, comp[nei])

                # low link same as index, so create SCC
                if low == index:
                    while new_node != node:
                        new_node = stack.pop()
                        comp[new_node] = index
                        top_order.append(new_node)
                else:
                    comp[node] = low

    top_order.reverse()
    return comp, top_order


class TwoSat:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(2 * n)]

    def _imply(self, x, y):
        self.graph[x].append(y if y >= 0 else 2 * self.n + y)

    def either(self, x, y):
        """either x or y must be True"""
        self._imply(~x, y)
        self._imply(~y, x)

    def set(self, x):
        """x must be True"""
        self._imply(~x, x)

    def solve(self):
        comp, top_order = scc(self.graph)
        for x in range(self.n):
            if comp[x] == comp[~x]:
                return False, None

        self.values = [None] * self.n
        for x in reversed(top_order):
            y = x if x < self.n else (2 * self.n - 1 - x)
            if self.values[y] is None:
                self.values[y] = x < self.n
        return True, self.values
