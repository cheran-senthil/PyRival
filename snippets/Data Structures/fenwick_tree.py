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
