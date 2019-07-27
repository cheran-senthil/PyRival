def pi(s):
    p = [0] * len(s)
    for i in range(1, len(s)):
        g = p[i - 1]
        while g and (s[i] != s[g]):
            g = p[g - 1]
        p[i] = g + (s[i] == s[g])

    return p


def match(s, pat, uniq='\0'):
    return [i + 1 - c for i, c in enumerate(pi(pat + uniq + s)[len(pat) + 1:]) if c == len(pat)]
