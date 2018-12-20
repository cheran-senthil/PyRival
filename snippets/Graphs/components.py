def connected_components(n, graph):
    components, visited = [], [False] * n

    def dfs(start):
        component, stack = [], [start]

        while stack:
            start = stack[-1]

            if visited[start]:
                stack.pop()
                continue
            else:
                visited[start] = True
                component.append(start)

            for i in graph[start]:
                if not visited[i]:
                    stack.append(i)

        return component

    for i in range(n):
        if not visited[i]:
            components.append(dfs(i))

    return components
