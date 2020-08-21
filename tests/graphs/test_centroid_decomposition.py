from pyrival.centroid_decomposition import *
import random

def test_small_centroids():
    t = 100000
    for _ in range(t):
        n = random.randint(1, 10)
        graph = [[] for _ in range(n)]
        for i in range(1, n):
            j = random.randrange(i)
            graph[i].append(j)
            graph[j].append(i)

        # Calculate number of pairs of nodes in the graph
        total = 0
        counter1 = 0
        counter2 = 0

        DP = [-1] * n
        for centroid in centroid_decomposition(graph):
            bfs = [centroid]

            for node in bfs:
                bfs += graph[node]
            
            counter1 += 1
            counter2 += len(bfs)

            for node in reversed(bfs):
                DP[node] = 1 + sum(DP[child] for child in graph[node])

            for child in graph[centroid]:
                total += (DP[centroid] - DP[child] + 1) * DP[child]
        
        assert counter1 == n
        assert counter2 <= n * (1 << n.bit_length())
        assert total == n * (n - 1)
        assert sum(len(c) for c in graph) == n - 1
