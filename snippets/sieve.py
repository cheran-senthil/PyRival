import array
from itertools import compress
from math import sqrt


class bitArray:
    def __init__(self, bit_size, fill=0):
        intSize = bit_size >> 5
        if (bit_size & 31):
            intSize += 1
        if fill == 1:
            fill = 4294967295
        else:
            fill = 0

        self.bit_size = bit_size
        self.bitArray = array.array('I')
        self.bitArray.extend((fill,) * intSize)

    def __getitem__(self, bit_num):
        if isinstance(bit_num, slice):
            return [self[i] for i in range(*bit_num.indices(self.bit_size))]
        record = bit_num >> 5
        offset = bit_num & 31
        mask = 1 << offset
        return((self.bitArray[record] & mask) >> offset)

    def __setitem__(self, bit_num, value):
        if isinstance(bit_num, slice):
            for i in range(*bit_num.indices(self.bit_size)):
                self[i] = value[i]
            return
        if value:
            self.setBit(bit_num)
        else:
            self.clearBit(bit_num)

    def setBit(self, bit_num):
        record = bit_num >> 5
        offset = bit_num & 31
        mask = 1 << offset
        self.bitArray[record] |= mask

    def clearBit(self, bit_num):
        record = bit_num >> 5
        offset = bit_num & 31
        mask = ~(1 << offset)
        self.bitArray[record] &= mask

    def toggleBit(self, bit_num):
        record = bit_num >> 5
        offset = bit_num & 31
        mask = 1 << offset
        self.bitArray[record] ^= mask


def get_primes(n):
    # does not return 2
    sieve = bytearray([True]) * (n//2 + 1)
    for i in range(1, int(sqrt(n))//2 + 1):
        if sieve[i]:
            sieve[2*i*(i+1)::2*i + 1] = bytearray((n//2 - 2*i*(i+1))//(2*i + 1) + 1)
    return compress(range(3, n + 1, 2), sieve[1:])


def get_primes2(n):
    # does not return 2 and 3
    correction = n % 6 > 1
    n = n + 6 - (n % 6)
    sieve = bitArray(n // 3, 1)
    clear = sieve.clearBit
    for i in range(1, int(sqrt(n) // 3 + 1)):
        if sieve[i]:
            k = (3 * i + 1) | 1
            for j in range(k * k // 3, n // 3, 2 * k):
                clear(j)
            for j in range(k * (k - 2 * (i & 1) + 4) // 3, n // 3, 2 * k):
                clear(j)

    #return sieve
    return ((3*i + 1) | 1 for i in range(1, n//3 - correction) if sieve[i])
