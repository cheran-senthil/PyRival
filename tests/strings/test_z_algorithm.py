from itertools import product
from random import choice, randrange
from string import ascii_lowercase

from pyrival.strings.z_algorithm import z_function


def test_z_algorithm__corner_cases():
    for n in range(1, 11):
        for word in product('abc', repeat=n):
            word = ''.join(c for c in word)
            assert z_function(word) == [_get_lcp(word, i) for i in range(n)]


def test_z_algorithm__large_cases():
    for c in range(1, 4):
        n = 10**5
        text = ''.join(choice(ascii_lowercase[:c]) for _ in range(n))

        z_array = z_function(text)
        for _ in range(100):
            i = randrange(n)
            assert z_array[i] == _get_lcp(text, i)

    n = 10**6
    f = lambda x: 'a' if bin(x).count('1') % 2 == 0 else 'b'
    text = ''.join(f(i) for i in range(n))

    z_array = z_function(text)
    for _ in range(100):
        i = randrange(n)
        assert z_array[i] == _get_lcp(text, i)


def _get_lcp(text, i):
    n = len(text)

    z = 0
    while i + z < n and text[i + z] == text[z]:
        z += 1

    return z
