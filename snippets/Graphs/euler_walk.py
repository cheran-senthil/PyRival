def euler_walk(n, adj):
    deg = [0] * n

    for i in range(n):
        for j in range(n):
            deg[i] += adj[i][j]

    first = 0
    while deg[first] == 0:
        first += 1

    v1, v2 = -1, -1
    bad = False

    for i in range(n):
        if deg[i] % 2 == 1:
            if v1 == -1:
                v1 = i
            elif v2 == -1:
                v2 = i
            else:
                bad = True

    if v1 != -1:
        adj[v1][v2] += 1
        adj[v2][v1] += 1

    st, res = [first], []

    while st:
        v = st[-1]
        flag = False

        for i in range(n):
            if adj[v][i]:
                flag = True
                break

        if flag:
            adj[v][i] -= 1
            adj[i][v] -= 1
            st.append(i)
        else:
            res.append(v)
            st.pop()

    if v1 != -1:
        for i in range(len(res) - 1):
            if ((res[i] == v1) and (res[i + 1] == v2)) or ((res[i] == v2) and (res[i + 1] == v1)):
                res = [res[j] for j in range(i + 1, len(res))] + [res[j] for j in range(1, i + 1)]
                break

    for i in range(n):
        for j in range(n):
            if adj[i][j]:
                bad = True

    if bad:
        return None

    return res
