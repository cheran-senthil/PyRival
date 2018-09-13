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
def lps(s):
    if len(s) < 2:
        return type(s)(s)
    if s[0] == s[-1]:
        return type(s)(s[0]) + lps(s[1:-1]) + type(s)(s[-1])
    return max(lps(s[1:]), lps(s[:-1]), key=len)
