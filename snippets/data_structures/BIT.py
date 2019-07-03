class FenwickTree(object):
    def __init__(self, x):
        self.bit = x
        """transform list into BIT"""
        for i in range(len(x)):
            j = i | (i + 1)
            if j < len(x):
                x[j] += x[i]

    def update(self, idx, x):
        """updates bit[idx] += x"""
        bit = self.bit
        while idx < len(bit):
            bit[idx] += x
            idx |= idx + 1

    def query(self, end):
        """calc sum(bit[:end])"""
        bit = self.bit
        x = 0
        while end:
            x += bit[end - 1]
            end &= end - 1
        return x

    def findkth(self, k):
        """Find largest idx such that sum(bit[:idx]) <= k"""
        bit = self.bit
        idx = -1
        for d in reversed(range(len(bit).bit_length())):
            right_idx = idx + (1 << d)
            if right_idx < len(bit) and k >= bit[right_idx]:
                idx = right_idx
                k -= bit[idx]
        return idx + 1
