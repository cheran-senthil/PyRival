"""
Given an undirected graph,
 
  1   4   7   10
 / \ / \ / \ /
2   0   5   9
 \ / \ / \ /
  3   6   8
 
the cut_tree function returns the cut-block tree made out of 2 sets of nodes, the original
nodes U in the graph and new nodes V corresponding to each node biconnected component. 
There is an edge between (u,v) for u in U and v in V if u lies in bicomponent v. 
In the case of an unconnected graph, the function returns a forest of block-cut trees.
For the graph above, this is the tree returned by cut_tree
 
    1        4        7        10
    |        |        |        |
2--(14)--0--(13)--5--(12)--9--(11)
    |        |        | 
    3        6        8
 
Here the nodes in () denotes bicomponent nodes.
"""
def cut_tree(graph):
    n = len(graph)
    new_graph = [[] for _ in range(n)]
 
    P = [-1] * n
    depth = [-1] * n
    biconnect = [None] * n
    root = 0
 
    preorder = []
    stack = [root]
    while stack:
        node = stack.pop()
        if depth[node] >= 0:
            continue
        depth[node] = len(preorder)
        preorder.append(node)
        for nei in graph[node]:
            if depth[nei] == -1:
                P[nei] = node
                stack.append(nei)
    preorder.pop(0)
 
    for node in reversed(preorder):
        depth[node] = min(depth[nei] for nei in graph[node]) 
        if depth[P[node]] == depth[node]:
            bicon = biconnect[node] = [P[node], node]
            new_graph.append(bicon)
   
    for node in preorder:
        if biconnect[node] is None:
            bicon = biconnect[node] = biconnect[P[node]]
            bicon.append(node)
    
    for bicon_ind in range(n, len(new_graph)):
        for node in new_graph[bicon_ind]:
            new_graph[node].append(bicon_ind)
 
    return new_graph
