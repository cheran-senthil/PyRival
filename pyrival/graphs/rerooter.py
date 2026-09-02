# for usage see https://codeforces.com/blog/entry/124286

def rerooter(graph, default, combine, finalize=lambda nodeDP, node, eind: nodeDP):
    n = len(graph)
    rootDP = [0] * n
    forwardDP = [None] * n
    reverseDP = [None] * n

    def exclusive(A, zero, combine, node):
        n = len(A)
        exclusiveA = [zero] * n

        for bit in range(n.bit_length())[::-1]:
            for i in range(n)[::-1]:
                exclusiveA[i] = exclusiveA[i // 2]
            for i in range(n & (-1 if bit else -2)):
                ind = (i >> bit) ^ 1
                exclusiveA[ind] = combine(exclusiveA[ind], A[i], node, i)
        return exclusiveA

    DP = [0] * n
    bfs = [0]
    P = [0] * n
    for node in bfs:
        for nei in graph[node]:
            if P[node] != nei:
                P[nei] = node
                bfs.append(nei)

    for node in reversed(bfs):
        nodeDP = default[node]
        for eind, nei in enumerate(graph[node]):
            if P[node] != nei:
                nodeDP = combine(nodeDP, DP[nei], node, eind)
        DP[node] = finalize(nodeDP, node, graph[node].index(P[node]) if node else -1)

    for node in bfs:
        DP[P[node]] = DP[node]
        forwardDP[node] = [DP[nei] for nei in graph[node]]
        rerootDP = exclusive(forwardDP[node], default[node], combine, node)
        reverseDP[node] = [
            finalize(nodeDP, node, eind) for eind, nodeDP in enumerate(rerootDP)
        ]
        rootDP[node] = finalize(
            (
                combine(rerootDP[0], forwardDP[node][0], node, 0)
                if n > 1
                else default[node]
            ),
            node,
            -1,
        )
        for nei, dp in zip(graph[node], reverseDP[node]):
            DP[nei] = dp
    return rootDP, forwardDP, reverseDP
