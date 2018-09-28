from pickle import dumps


class MemoizeMutable:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}

    def __call__(self, *args, **kwds):
        key = dumps(args, 1) + dumps(kwds, 1)
        if not (key in self.memo):
            self.memo[key] = self.fn(*args, **kwds)

        return self.memo[key]


@MemoizeMutable
def lcs(s1, s2):
    if (not s1) or (not s2):
        return []

    return (
        lcs(s1[:-1], s2[:-1]) + [s1[-1]]
        if s1[-1] == s2[-1] else
        max(lcs(s1[:-1], s2), lcs(s1, s2[:-1]), key=len)
    )


def lis(arr):
    return lcs(arr, sorted(arr))
