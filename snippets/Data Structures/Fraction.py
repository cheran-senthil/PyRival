from math import gcd


class Fraction:
    """ A class to represent rational numbers. """

    def __init__(self, num=0, den=1):
        g = gcd(num, den)
        self.num = int(num > 0) - int(num < 0) if g == 0 else num // g
        self.den = 0 if g == 0 else den // g

    def __floor__(self):
        return self.num // self.den

    def __ceil__(self):
        return (self.num + self.den - 1) // self.den

    def __round__(self, ndigits):
        return round(self.num / self.den, ndigits)

    def __hash__(self):
        return hash((self.num, self.den))

    def __eq__(self, other):
        return (self.num, self.den) == (other.num, other.den)

    def __ne__(self, other):
        return not (self == other)
