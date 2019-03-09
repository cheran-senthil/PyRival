def LPSubstr(s):
    n = len(s)
    p = [[0] * (n + 1), [0] * n]

    for z, p_z in enumerate(p):
        left, right = 0, 0
        for i in range(n):
            t = right - i + 1 - z
            if i < right:
                p_z[i] = min(t, p_z[left + t])
            L, R = i - p_z[i], i + p_z[i] - 1 + z
            while (L >= 1) and (R + 1 < n) and (s[L - 1] == s[R + 1]):
                p_z[i] += 1
                L -= 1
                R += 1
            if R > right:
                left, right = L, R

    i1, x1 = max(enumerate(p[0]), key=lambda x: x[1])
    i2, x2 = max(enumerate(p[1]), key=lambda x: x[1])

    return s[i1 - x1:i1 + x1], s[i2 - x2:i2 + x2 + 1]
