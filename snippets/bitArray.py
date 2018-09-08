import array


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
