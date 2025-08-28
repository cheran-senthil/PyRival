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


# Edge-bcc uses pyrivals scc.py as a subroutine
"""
Given a directed graph, find_SCC returns a list of lists containing 
the strongly connected components in topological order.

Note that this implementation can be also be used to check if a directed graph is a
DAG, and in that case it can be used to find the topological ordering of the nodes.
"""

def find_SCC(graph):
    SCC, S, P = [], [], []
    depth = [0] * len(graph)
 
    stack = list(range(len(graph)))
    while stack:
        node = stack.pop()
        if node < 0:
            d = depth[~node] - 1
            if P[-1] > d:
                SCC.append(S[d:])
                del S[d:], P[-1]
                for node in SCC[-1]:
                    depth[node] = -1
        elif depth[node] > 0:
            while P[-1] > depth[node]:
                P.pop()
        elif depth[node] == 0:
            S.append(node)
            P.append(len(S))
            depth[node] = len(S)
            stack.append(~node)
            stack += graph[node]
    return SCC[::-1]


"""
Given an undirected simple graph, find_BCC returns a list of lists 
containing the edge biconnected components of the graph (i.e. no bridges).
Runs in O(n + m) time.

This algorithm is based on https://cses.fi/problemset/task/2177
"""
def find_BCC(graph):
    d = 0
    depth = [0] * len(graph)
    stack = list(range(len(graph)))
    while stack:
        node = stack.pop()
        if node < 0:
            d -= 1
        elif not depth[node]:
            d = depth[node] = d + 1
            stack.append(~node)
            stack += graph[node]
    
    graph2 = [[v for v in g if d + 2 > depth[v] != d - 1] for g,d in zip(graph, depth)]
    return find_SCC(graph2)
