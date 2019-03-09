def least_rotation(s):
    a, n = 0, len(s)
    s += s

    for b in range(n):
        for i in range(n):
            if (a + i == b) or (s[a + 1] < s[b + i]):
                b += max(0, i - 1)
                break
            if s[a + i] > s[b + i]:
                a = b
                break

    return s[a:a + n]
