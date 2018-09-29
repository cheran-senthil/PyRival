from fractions import Fraction


def CFraction(frac):
    num = frac.numerator
    den = frac.denominator
    yield num // den
    num %= den
    while den != 1:
        num, den = den, num
        yield num // den
        num %= den


def CFrac2Frac(cfrac):
    num, den = 1, 0
    for u in reversed(cfrac):
        num, den = den + num*u, num
    return Fraction(num, den)
