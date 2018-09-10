from operator import rshift

class bitArray:
    def __init__(self, size):
        self.bytes = bytearray(rshift(size, 3) + 1)

    def __getitem__(self, index):
        return rshift(self.bytes[rshift(index, 3)], (index & 0b111)) & 1

    def __setitem__(self, index, value):
        if value:
            self.bytes[rshift(index, 3)] |= 1 << (index & 0b111)
        else:
            self.bytes[rshift(index, 3)] &= ~(1 << (index & 0b111))
