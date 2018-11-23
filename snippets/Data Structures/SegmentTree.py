class SegmentTree:
    def __init__(self, m, d=0, func=max, low=-float('inf')):
        self.n = 1 << m.bit_length()
        self.s = [d if i < self.n + m else low for i in range(2*self.n)]
        self.func = func
        self.low = low

        for i in range(self.n - 1, 0, -1):
            self.s[i] = func(self.s[2*i], self.s[2*i + 1])

    def __setitem__(self, pos, val):
        pos += self.n
        self.s[pos] = val
        pos //= 2
        while pos >= 1:
            self.s[pos] = self.func(self.s[2*pos], self.s[2*pos + 1])
            pos //= 2

    def __getitem__(self, pos):
        return self.query(pos, pos + 1)

    def que(self, pos, left, right, lo, hi):
        if (right <= lo) or (hi <= left):
            return self.low
        if (left <= lo) and (hi <= right):
            return self.s[pos]

        return self.func(self.que(2 * pos, left, right, lo, (lo + hi) / 2),
                         self.que(2*pos + 1, left, right, (lo + hi) / 2, hi))

    def query(self, left, right):
        return self.que(1, left, right, 0, self.n)
