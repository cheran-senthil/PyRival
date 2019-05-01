class LazySegmentTree:
    def __init__(self, data):
        """maximum segment tree"""
        self.m = m = 1 << (len(data) - 1).bit_length()
        self.data = [0] * (2 * m)
        self.data[m:m + len(data)] = data
        for i in reversed(range(m)):
            self.data[i] = max(self.data[2 * i], self.data[2 * i + 1])
        self.query = [0] * (2 * m)

    def push(self, seg_ind):
        """push the query on seg_ind to its children"""
        # Let the children know of the queries
        q = self.query[seg_ind]

        self.query[2 * seg_ind] += q
        self.query[2 * seg_ind + 1] += q

        self.data[2 * seg_ind] += q
        self.data[2 * seg_ind + 1] += q

        # Remove queries from seg_ind
        self.data[seg_ind] = max(self.data[2 * seg_ind], self.data[2 * seg_ind + 1])
        self.query[seg_ind] = 0

    def update(self, seg_ind):
        """updates the node seg_ind to know of all queries applied to it via its ancestors"""
        # Find all indecies to be updated
        seg_ind >>= 1
        inds = []
        while seg_ind > 0:
            inds.append(seg_ind)
            seg_ind >>= 1

        # Push the queries down the segment tree
        for ind in reversed(inds):
            self.push(ind)

    def build(self, seg_ind):
        """make the changes to seg_ind be known to its ancestors"""
        seg_ind >>= 1
        while seg_ind > 0:
            self.data[seg_ind] = max(self.data[2 * seg_ind], self.data[2 * seg_ind + 1]) + self.query[seg_ind]
            seg_ind >>= 1

    def add(self, start, end, value):
        """lazily add value to [start, end)"""
        start += self.m
        end += self.m
        _start, _end = start, end

        while _start < _end:
            if _start & 1:
                self.query[_start] += value
                self.data[_start] += value
                _start += 1

            if _end & 1:
                _end -= 1
                self.query[_end] += value
                self.data[_end] += value

            _start >>= 1
            _end >>= 1

        # Tell all nodes above of the updated area of the updates
        self.build(start)
        self.build(end - 1)

    def maxi(self, start, end):
        """max of data[start, end)"""
        start += self.m
        end += self.m

        # Apply all the lazily stored queries
        self.update(start)
        self.update(end - 1)
        segs = []

        while start < end:
            if start & 1:
                segs.append(start)
                start += 1

            if end & 1:
                end -= 1
                segs.append(end)

            start >>= 1
            end >>= 1

        return max(self.data[i] for i in segs)
