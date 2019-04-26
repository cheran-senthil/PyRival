def memoize(f):
    """memoization decorator for a function taking one or more arguments"""

    class memodict(dict):
        def __getitem__(self, *key):
            return dict.__getitem__(self, key)

        def __missing__(self, key):
            ret = self[key] = f(*key)
            return ret

    return memodict().__getitem__


@memoize
def partition(n, k):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if k < 1:
        return 0
    if n == 1:
        return 1
    return partition(n, k - 1) + partition(n - k, k)
