from bisect import bisect_left


class FenwickTree:
    def __init__(self, n):
        self.s = [0] * n

    def update(self, pos, dif):
        while pos < len(self.s):
            self.s[pos] += dif
            pos |= pos + 1

    def query(self, pos):
        res = 0
        while pos > 0:
            res += self.s[pos - 1]
            pos &= pos - 1
        return res

    def lower_bound(self, val):
        if val <= 0:
            return -1

        pos = 0

        pw = 1 << len(self.s).bit_length()
        while pw != 0:
            if pw + pos <= len(self.s):
                if self.s[pos + pw - 1] < val:
                    pos += pw
                    val -= self.s[pos - 1]
            pw >>= 1

        return pos


class FenwickTree2d:
    def __init__(self, points, difs, n=100000):
        self.ys = [[] for _ in range(n)]
        self.ft = []

        for point in points:
            x, y = point
            while x < len(self.ys):
                self.ys[x].append(y)
                x |= x + 1

        for v in self.ys:
            v.sort()
            self.ft.append(FenwickTree(len(v)))

        for point, dif in zip(points, difs):
            x, y = point
            while x < len(self.ys):
                self.ft[x].update(bisect_left(self.ys[x], y), dif)
                x |= x + 1

    def query(self, point):
        x, y = point
        res = 0
        while x != 0:
            res += self.ft[x - 1].query(bisect_left(self.ys[x - 1], y))
            x &= x - 1
        return res
