# A very nice implementation of a maximum segment tree with
# some inspiration taken from https://codeforces.com/blog/entry/18051
# This implementation should be able to be modified to do pretty
# much anything one would want to do with segment trees apart from
# persistance.
# Note that especially in python this implementation is much much better
# than most other approches because how slow python can be with function
# calls.

# Currently it allows for two operations, both running in O(log n),
# 'add(l,r,value)' adds value to [l,r)
# 'maxi(l,r)' returns the biggest value on l:r


class SegmentTree:
    def __init__(self, data):
        n = len(data)
        m = 1
        while m < n:
            m *= 2

        self.n = n
        self.m = m
        self.data = [0] * (2 * m)
        for i in range(n):
            self.data[i + m] = data[i]
        for i in reversed(range(m)):
            self.data[i] = max(self.data[2 * i], self.data[2 * i + 1])
        self.query = [0] * (2 * m)

    # Push the query on seg_ind to its children
    def push(self, seg_ind):
        # Let the children know of the queries
        q = self.query[seg_ind]

        self.query[2 * seg_ind] += q
        self.query[2 * seg_ind + 1] += q

        self.data[2 * seg_ind] += q
        self.data[2 * seg_ind + 1] += q

        # Remove queries from seg_ind
        self.data[seg_ind] = max(self.data[2 * seg_ind],
                                 self.data[2 * seg_ind + 1])
        self.query[seg_ind] = 0

    # Updates the node seg_ind to know of all queries
    # applied to it via its ancestors
    def update(self, seg_ind):
        # Find all indecies to be updated
        seg_ind //= 2
        inds = []
        while seg_ind > 0:
            inds.append(seg_ind)
            seg_ind //= 2

        # Push the queries down the segment tree
        for ind in reversed(inds):
            self.push(ind)

    # Make the changes to seg_ind be known to its ancestors
    def build(self, seg_ind):
        seg_ind //= 2
        while seg_ind > 0:
            self.data[seg_ind] = max(
                self.data[2 * seg_ind],
                self.data[2 * seg_ind + 1]) + self.query[seg_ind]
            seg_ind //= 2

    # Lazily add value to [l,r)
    def add(self, l, r, value):
        l += self.m
        r += self.m

        l0 = l
        r0 = r

        while l < r:
            if l % 2 == 1:
                self.query[l] += value
                self.data[l] += value
                l += 1
            if r % 2 == 1:
                r -= 1
                self.query[r] += value
                self.data[r] += value
            l //= 2
            r //= 2

        # Tell all nodes above of the updated
        # area of the updates
        self.build(l0)
        self.build(r0 - 1)

    # Max of data[l,r)
    def maxi(self, l, r):
        l += self.m
        r += self.m

        # Apply all the lazily stored queries
        self.update(l)
        self.update(r - 1)

        segs = []
        while l < r:
            if l % 2 == 1:
                segs.append(l)
                l += 1
            if r % 2 == 1:
                r -= 1
                segs.append(r)
            l //= 2
            r //= 2

        return max(self.data[ind] for ind in segs)
