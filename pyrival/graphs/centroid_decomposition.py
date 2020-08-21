def centroid_decomposition(graph):
    """ 
    Given a tree, this function is a generator that
    1. Roots the tree at its centroid (modifying graph)
    2. Yields centroid
    3. Removes centroid from the graph
    4. Recurses on the forest left after the removal
    
    This generator makes working with centroid decomposition easy. It yields the n 
    centroids involved in the decomposition. It also keeps the graph rooted at the yielded
    centroid by modifying the input variable graph. In total this takes O(n log n) time.

    Input:
      graph: list of lists where graph[u] is a list containing all neighbours of node u
    
    Example:
      >>> graph = [[1], [0,2], [1]]
      >>> for centroid in centroid_decomposition(graph):
      >>>   bfs = [centroid]
      >>>   for node in bfs:
      >>>     bfs += graph[node] # Valid since graph is rooted at the centroid
      >>>   print('BFS from centroid:', bfs)
      BFS from centroid: [1, 0, 2]
      BFS from centroid: [0]
      BFS from centroid: [2]
    """
    n = len(graph)
    
    bfs = [n - 1]
    for node in bfs:
        bfs += graph[node]
        for nei in graph[node]:
            graph[nei].remove(node)
    
    size = [0] * n
    for node in reversed(bfs):
        size[node] = 1 + sum(size[child] for child in graph[node])
 
    def reroot_centroid(root):
        N = size[root]
        while True:
            for child in graph[root]:
                if size[child] > N // 2:
                    size[root] = N - size[child]
                    graph[root].remove(child)
                    graph[child].append(root)
                    root = child
                    break
            else:
                return root
        
    bfs = [n - 1]
    for node in bfs:
        centroid = reroot_centroid(node)
        bfs += graph[centroid]
        yield centroid
