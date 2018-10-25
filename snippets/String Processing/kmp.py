def kmpSearch(T, P):
    b = [-1] * (len(P) + 1)

    j = -1
    for i in range(len(P)):
        while (j >= 0) and (P[i] != P[j]):
            j = b[j]
        j += 1
        b[i+1] = j

    j = 0
    for i in range(len(T)):
        while (j >= 0) and (T[i] != P[j]):
            j = b[j]
        j += 1
        if j == m:
            yield i + 1 - j
            j = b[j]
