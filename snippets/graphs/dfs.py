def dfs(graph, start=0):
    n = len(graph)

    dp = [0] * n
    visited, finished = [False] * n, [False] * n

    stack = [start]
    while stack:
        start = stack[-1]

        # push unvisited children into stack
        if not visited[start]:
            visited[start] = True
            for child in graph[start]:
                if not visited[child]:
                    stack.append(child)

        else:
            stack.pop()

            # base case
            dp[start] += 1

            # update with finished children
            for child in graph[start]:
                if finished[child]:
                    dp[start] += dp[child]

            finished[start] = True

    return visited, dp
