"""
REMARK: There are two definitions of biconnectedness of an undirected graph, 
        either node-bcc or edge-bcc, corresponding to node_bbc.py and edge_bcc.py.

* In node-bcc, a "cut-vertex" (also called an articulation point) is a node where 
  removing it would split up the graph into multiple connected components.

* In edge-bcc, a "bridge" is an edge where removing it would split up the graph 
  into multiple connected components.

For example, this graph

  1   4   7   10
 / \ / \ / \ /
2   0   5   9
 \ / \ / \ /
  3   6   8

has three cut vertices (nodes 0,5,9) and one bridge (edge between 9 and 10).
The number of node-bcc = 4 and number of edge-bcc = 2.
Note that a node belongs to multiple node-bccs iff it is a cut-vertex.
"""

"""
Given a connected undirected graph, find_BCC returns a list of lists containing the nodes 
of the different node-biconnected components.
Note that a node belongs to multiple node-bccs iff it is an articulation point.

In the case that the given graph is unconnected, find_BCC finds the BCCs of the connected
component of 'root'.
"""

def find_BCC(graph, root=0):
    n = len(graph)
    BCC = []
 
    P = [-1] * n
    depth = [-1] * n
    biconnect = [None] * n
 
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
    
    if not preorder:
        return [[root]]
 
    for node in reversed(preorder):
        depth[node] = min(depth[nei] for nei in graph[node]) 
        if depth[P[node]] == depth[node]:
            bicon = biconnect[node] = [P[node], node]
            BCC.append(bicon)
   
    for node in preorder:
        if biconnect[node] is None:
            bicon = biconnect[node] = biconnect[P[node]]
            bicon.append(node)
    
    return BCC
