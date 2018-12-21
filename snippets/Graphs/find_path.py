def find_path(start, end, parents):
    """
    Constructs a path between two vertices, given the parents of all vertices.

    Parameters
    ----------
    start : int
        The first verex in the path
    end : int
        The last vertex in the path
    parents : list[int]
        The parent of a vertex in its path from start to end.

    Returns
    -------
    path : list[int]
        The path from start to end.
    """
    path, parent = [], end

    while parent != parents[start]:
        path.append(parent)
        parent = parents[parent]

    return path[::-1]
