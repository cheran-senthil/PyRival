from itertools import product
from random import randrange

from pyrival.strings.z_algorithm import z_function


def test_z_algorithm__corner_cases():
    for n in range(1, 11):
        for word in product('abc', repeat=n):
            assert z_function(word) == [_get_lcp(word, i) for i in range(n)]


def test_z_algorithm__large_cases():
    text = 'abaa' * 10**5
    z_array = z_function(text)

    for _ in range(100):
        i = randrange(len(text))
        assert z_array[i] == _get_lcp(text, i)

    f = lambda x: 'a' if bin(x).count('1') % 2 == 0 else 'b'
    text = ''.join(f(i) for i in range(10**6))
    z_array = z_function(text)

    for _ in range(100):
        i = randrange(len(text))
        assert z_array[i] == _get_lcp(text, i)


def _get_lcp(text, i):
    z = 0
    while i + z < len(text) and text[i + z] == text[z]:
        z += 1

    return z
