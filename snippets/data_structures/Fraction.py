from math import gcd


class Fraction:
    """ A class to represent rational numbers. """

    def __init__(self, num=0, den=1):
        g = gcd(num, den)
        self.num, self.den = num // g, den // g

    def __add__(self, other):
        num = self.num * other.den + other.num * self.den
        den = self.den * other.den
        g = gcd(num, den)
        return Fraction(num // g, den // g)

    def __sub__(self, other):
        num = self.num * other.den - other.num * self.den
        den = self.den * other.den
        g = gcd(num, den)
        return Fraction(num // g, den // g)

    def __mul__(self, other):
        num = self.num * other.num
        den = self.den * other.den
        g = gcd(num, den)
        return Fraction(num // g, den // g)

    def __truediv__(self, other):
        num = self.num * other.den
        den = self.den * other.num
        g = gcd(num, den)
        return Fraction(num // g, den // g)

    def __floordiv__(self, other):
        return (self.num * other.den) // (self.den * other.num)

    __pow__ = lambda self, other: Fraction(self.num**other, self.den**other)
    __bool__ = lambda self: bool(self.num)
    __int__ = lambda self: self.num // self.den
    __float__ = lambda self: self.num / self.den
    __abs__ = lambda self: self if self.num >= 0 else Fraction(-self.num, self.den)
    __neg__ = lambda self: Fraction(-self.num, self.den)
    __round__ = lambda self, ndigits: round(self.num / self.den, ndigits)
    __copy__ = lambda self: Fraction(self.num, self.den)
    __hash__ = lambda self: hash((self.num, self.den))

    __eq__ = lambda self, other: self.num * other.den == other.num * self.den
    __ne__ = lambda self, other: self.num * other.den != other.num * self.den
    __lt__ = lambda self, other: self.num * other.den < other.num * self.den
    __gt__ = lambda self, other: self.num * other.den > other.num * self.den
    __le__ = lambda self, other: self.num * other.den <= other.num * self.den
    __ge__ = lambda self, other: self.num * other.den >= other.num * self.den

    def limit_denominator(self, max_den=1000000):
        if self.den <= max_den:
            return self

        p0, q0, p1, q1 = 0, 1, 1, 0
        n, d = self.num, self.den
        while True:
            a = n // d
            q2 = q0 + a * q1
            if q2 > max_den:
                break
            p0, q0, p1, q1 = p1, q1, p0 + a * p1, q2
            n, d = d, n - a * d

        k = (max_den - q0) // q1
        bound1 = Fraction(p0 + k * p1, q0 + k * q1)
        bound2 = Fraction(p1, q1)
        return bound2 if abs(bound2 - self) <= abs(bound1 - self) else bound1
