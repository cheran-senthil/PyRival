from pickle import dumps


def memodict(f):
    """ Memoization decorator for a function taking a single argument """
    class memodict(dict):
        def __missing__(self, key):
            ret = self[key] = f(key)
            return ret
    return memodict().__getitem__


def memoize(f):
    """ Memoization decorator for a function taking one or more arguments. """
    class memodict(dict):
        def __getitem__(self, *key):
            return dict.__getitem__(self, key)

        def __missing__(self, key):
            ret = self[key] = f(*key)
            return ret

    return memodict().__getitem__


class MemoizeMutable:
    """ Memoization decorator for a function mutable arguments. """
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}

    def __call__(self, *args, **kwds):
        key = dumps(args, 1) + dumps(kwds, 1)
        if not (key in self.memo):
            self.memo[key] = self.fn(*args, **kwds)

        return self.memo[key]
