from pyrival.graphs.bfs import bfs


def test_bfs_returns_traversal_order():
    graph = [[1, 2], [0, 3], [0], [1]]
    assert bfs(graph) == [0, 1, 2, 3]
