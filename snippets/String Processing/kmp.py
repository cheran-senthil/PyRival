def pi(s):
    p = [0] * len(s)
    for i in range(1, len(s)):
        g = p[i - 1]
        while g and (s[i] != s[g]):
            g = p[g - 1]
        p[i] = g + int(s[i] == s[g])

    return p


def match(s, pat):
    res = []
    p = pi(pat + '\0' + s)
    for i in range(len(p) - len(s), len(p)):
        if p[i] == len(pat):
            res.append(i - 2 * len(pat))

    return res
