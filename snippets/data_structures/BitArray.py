class bitarray:
    """implements bitarray using bytearray"""

    def __init__(self, size):
        self.bytes = bytearray((size >> 3) + 1)

    def __getitem__(self, index):
        return (self.bytes[index >> 3] >> (index & 7)) & 1

    def __setitem__(self, index, value):
        if value:
            self.bytes[index >> 3] |= 1 << (index & 7)
        else:
            self.bytes[index >> 3] &= ~(1 << (index & 7))
