def least_rotation(s):
    a, n = 0, len(s)
    s = s + s

    b = 1
    while b < n:
        for i in range(b - a):
            if s[a + i] > s[b + i]:
                a = b
                b += 1
                break
            if s[a + i] < s[b + i]:
                b += i + 1
                break
        else:
            b += b - a
    return s[a:a + n]
