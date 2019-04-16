def find_path(start, end, parents):
    """ Constructs a path between two vertices, given the parents of all vertices. """
    path, parent = [], end

    while parent != parents[start]:
        path.append(parent)
        parent = parents[parent]

    return path[::-1]
