import operator as op


class BitArray:
    def __init__(self, size):
        self.bytes = bytearray(op.rshift(size, 3) + 1)

    def __getitem__(self, index):
        return op.rshift(self.bytes[op.rshift(index, 3)], (index & 0b111)) & 1

    def __setitem__(self, index, value):
        if value:
            self.bytes[op.rshift(index, 3)] |= 1 << (index & 0b111)
        else:
            self.bytes[op.rshift(index, 3)] &= ~(1 << (index & 0b111))
