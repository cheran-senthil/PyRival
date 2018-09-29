class SegmentTree:
    def __init__(self, m, d=0, func=max, low=-float('inf')):
        self.n = n = 1 << m.bit_length()
        self.s = s = [d if i < n + m else low for i in range(2*n)]
        self.func = func
        self.low = low

        for i in range(n - 1, 0, -1):
            s[i] = func(s[i * 2], s[i*2 + 1])

    def __setitem__(self, pos, val):
        pos += self.n
        self.s[pos] = val
        pos //= 2
        while pos >= 1:
            self.s[pos] = self.func(self.s[pos * 2], self.s[pos*2 + 1])
            pos //= 2

    def __getitem__(self, pos):
        return self.query(pos, pos + 1)

    def que(self, pos, l, r, lo, hi):
        if (r <= lo) or (hi <= l):
            return self.low
        if (l <= lo) and (hi <= r):
            return self.s[pos]

        return self.func(self.que(2 * pos, l, r, lo, (lo + hi) / 2),
                         self.que(2*pos + 1, l, r, (lo + hi) / 2, hi))

    def query(self, l, r):
        return self.que(1, l, r, 0, self.n)

