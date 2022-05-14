"""
The "sorted list" data-structure, with amortized O(n^(1/3)) cost per insert and pop.

Example:

A = SortedList()
A.insert(30)
A.insert(50)
A.insert(20)
A.insert(30)
A.insert(30)

print(A) # prints [20, 30, 30, 30, 50]

print(A.lower_bound(30), A.upper_bound(30)) # prints 1 4

print(A[-1]) # prints 50
print(A.pop(1)) # prints 30

print(A) # prints [20, 30, 30, 50]
print(A.count(30)) # prints 2

"""

from bisect import bisect_left as lower_bound, bisect_right as upper_bound 
 
class FenwickTree:
    def __init__(self, x):
        bit = self.bit = list(x)
        size = self.size = len(bit)
        for i in range(size):
            j = i | (i + 1)
            if j < size:
                bit[j] += bit[i]
 
    def update(self, idx, x):
        """updates bit[idx] += x"""
        while idx < self.size:
            self.bit[idx] += x
            idx |= idx + 1

    def __call__(self, end):
        """calc sum(bit[:end])"""
        x = 0
        while end:
            x += self.bit[end - 1]
            end &= end - 1
        return x

    def find_kth(self, k):
        """Find largest idx such that sum(bit[:idx]) <= k"""
        idx = -1
        for d in reversed(range(self.size.bit_length())):
            right_idx = idx + (1 << d)
            if right_idx < self.size and self.bit[right_idx] <= k:
                idx = right_idx
                k -= self.bit[idx]
        return idx + 1, k
 
 
block_size = 700
class SortedList:
    def __init__(self):
        self.macro = []
        self.micros = [[]]
        self.micro_size = [0]
        self.fenwick = FenwickTree([0])
        self.size = 0
 
    def insert(self, x):
        i = lower_bound(self.macro, x)
        j = upper_bound(self.micros[i], x)
        self.micros[i].insert(j, x)
        self.size += 1
        self.micro_size[i] += 1
        self.fenwick.update(i, 1)
        if len(self.micros[i]) >= block_size:
            self.micros[i : i + 1] = self.micros[i][:block_size >> 1], self.micros[i][block_size >> 1:]
            self.micro_size[i : i + 1] = block_size >> 1, block_size >> 1
            self.fenwick = FenwickTree(self.micro_size)
            self.macro.insert(i, self.micros[i + 1][0])
    
    def pop(self, k=0):
        i,j = self._find_kth(k)
        x = self.micros[i].pop(j)
        self.size -= 1
        self.micro_size[i] -= 1
        self.fenwick.update(i, -1)
        return x
    
    def __getitem__(self, k):
        i,j = self._find_kth(k)
        return self.micros[i][j]
 
    def __contains__(self, x):
        i = lower_bound(self.macro, x)
        j = lower_bound(self.micros[i], x)
        i,j = (i, j) if j < self.micro_size[i] else (i + 1, 0)
        return i < len(self.micros) and j < self.micros_size[i] and self.micros[i][j] == x
    
    def lower_bound(self, x):
        i = lower_bound(self.macro, x)
        return self.fenwick(i) + lower_bound(self.micros[i], x)
    
    def upper_bound(self, x):
        i = upper_bound(self.macro, x)
        return self.fenwick(i) + upper_bound(self.micros[i], x)
    
    def _find_kth(self, k):
        return self.fenwick.find_kth(k + self.size if k < 0 else k)
    
    def __len__(self):
        return self.size
    
    def __iter__(self):
        return (x for micro in self.micros for x in micro)
    
    def __repr__(self):
        return str(list(self))

    def count(self, x):
        return self.upper_bound(x) - self.lower_bound(x)
