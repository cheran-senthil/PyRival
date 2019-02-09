import itertools


class RangeQuery(object):
    def __init__(self, items, func=min):
        self.rq = rq = {(i, 0): item for i, item in enumerate(items)}
        self.func = func
        n = len(items)
        for step, i in itertools.product(range(1, n.bit_length()), range(n)):
            j = i + (1 << (step - 1))
            rq[i, step] = func(rq[i, step - 1],
                               rq[j, step - 1]) if j < n else rq[i, step - 1]

    def query(self, start, stop):
        j = (stop - start).bit_length() - 1
        return self.func(self.rq[start, j], self.rq[stop - (1 << j), j])
