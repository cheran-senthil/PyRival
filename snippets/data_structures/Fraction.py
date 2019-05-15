from math import gcd


class Fraction:
    def __init__(self, num=0, den=1):
        g = gcd(num, den)
        self.num, self.den = num // g, den // g

    __add__ = lambda self, other: Fraction(self.num * other.den + other.num * self.den, self.den * other.den)
    __sub__ = lambda self, other: Fraction(self.num * other.den - other.num * self.den, self.den * other.den)
    __mul__ = lambda self, other: Fraction(self.num * other.num, self.den * other.den)
    __truediv__ = lambda self, other: Fraction(self.num * other.den, self.den * other.num)
    __floordiv__ = lambda self, other: (self.num * other.den) // (self.den * other.num)

    __pow__ = lambda self, other: Fraction(self.num**other, self.den**other)
    __abs__ = lambda self: self if self.num >= 0 else Fraction(-self.num, self.den)
    __neg__ = lambda self: Fraction(-self.num, self.den)
    __round__ = lambda self, ndigits: round(self.num / self.den, ndigits)

    __bool__ = lambda self: bool(self.num)
    __int__ = lambda self: self.num // self.den
    __float__ = lambda self: self.num / self.den
    __str__ = lambda self: '(%s, %s)' % (self.num, self.den)

    __copy__ = lambda self: Fraction(self.num, self.den)
    __hash__ = lambda self: hash((self.num, self.den))

    __eq__ = lambda self, other: self.num * other.den == other.num * self.den
    __ne__ = lambda self, other: self.num * other.den != other.num * self.den
    __lt__ = lambda self, other: self.num * other.den < other.num * self.den
    __gt__ = lambda self, other: self.num * other.den > other.num * self.den
    __le__ = lambda self, other: self.num * other.den <= other.num * self.den
    __ge__ = lambda self, other: self.num * other.den >= other.num * self.den

    __repr__ = lambda self: 'Fraction(%s, %s)' % (self.num, self.den)


def limit_denominator(frac, max_den=1000000):
    if frac.den <= max_den:
        return frac

    p0, q0, p1, q1 = 0, 1, 1, 0
    n, d = frac.num, frac.den
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
    return bound2 if abs(bound2 - frac) <= abs(bound1 - frac) else bound1
