class BitArray:
    """
    A class to repesent fixed-size sequence of bits.

    Parameters
    ----------
    size : int
        The number of bits to allocate storage for.
    """

    def __init__(self, size):
        self.bytes = bytearray((size >> 3) + 1)

    def __getitem__(self, index):
        return (self.bytes[index >> 3] >> (index & 7)) & 1

    def __setitem__(self, index, value):
        if value:
            self.bytes[index >> 3] |= 1 << (index & 7)
        else:
            self.bytes[index >> 3] &= ~(1 << (index & 7))
