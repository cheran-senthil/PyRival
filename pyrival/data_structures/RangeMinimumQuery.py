"""
Range Minimum Query (RMQ), also known as sparse table.
Precomputation takes O(n log n) time and memory.
Query takes O(1) time.

To switch to a max version, simply search replace min to max.
"""
class RangeMinimumQuery:
    def __init__(self, data):
        self._data = [data]
        n = len(data)
        for bit in range(n.bit_length() - 1):
            i = 1 << bit
            data = [min(data[j], data[j + i]) for j in range(n - 2 * i + 1)]
            self._data.append(data)
 
    def query(self, start, stop):
        """min of data[start, stop)"""
        data = self._data[depth := (stop - start).bit_length() - 1]
        return min(data[start], data[stop - (1 << depth)])



"""
"Improved" Range Minimum Query (RMQ) based on https://codeforces.com/blog/entry/78931
Uses the above RMQ as a subroutine.

Precomputation takes O(n) time and memory.
Query takes O(1) time (but is slightly slower than above RMQ!).

To switch to a max version, simply search replace min to max in both RMQs.
"""
class RangeMinimumQuery2:
    def __init__(self, data):
        self.data = data
        n = len(data)
        mask = 0
        self.A = A = [0] * n
        for i in range(n)[::-1]:
            while mask and min(data[i + (mask & -mask).bit_length()], data[i]) == data[i]:
                mask &= mask - 1
            A[i] = mask = 2 * (mask & ~(-1<<62)) + 1
        self.B = [data[i + (A[i] & ~(-1<<32)).bit_length() - 1] for i in range(n)]
        self.RMQ = RangeMinimumQuery(self.B[::32])
    
    def __call__(self, start, stop):
        """min of data[start, stop)"""
        if stop - start <= 63:
            return self.data[start + (self.A[start] & ~(-1 << stop - start)).bit_length() - 1]
        return min(self.B[start], self.B[stop - 32], self.RMQ.query((start + 31) >> 5, stop >> 5))
