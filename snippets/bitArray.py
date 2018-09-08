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

        self.bitArray = array.array('I')
        self.bitArray.extend((fill,) * intSize)

    def __getitem__(self, bit_num):
        record = bit_num >> 5
        offset = bit_num & 31
        mask = 1 << offset
        return(self.bitArray[record] & mask)

    def __setitem__(self, bit_num, value):
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
