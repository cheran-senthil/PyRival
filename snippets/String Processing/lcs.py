def memodict(f):
    """ Memoization decorator for a function taking a single argument """
    class memodict(dict):
        def __missing__(self, key):
            ret = self[key] = f(key)
            return ret
    return memodict().__getitem__


@memodict
def lcs(s):
    """ s = (s1, s2) """
    s1, s2 = s
    if not s1 or not s2:
        return ''

    return (
        lcs((s1[:-1], s2[:-1])) + s1[-1]
        if s1[-1] == s2[-1] else
        max(lcs((s1[:-1], s2)), lcs((s1, s2[:-1])), key=len)
    )
