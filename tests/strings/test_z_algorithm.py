from random import choice
from itertools import product
from string import ascii_lowercase

from pyrival.strings.z_algorithm import z_function


def brute_force(text, limit=2**30):
    k = min(limit, len(text))
    z_array = [0] * k

    for i in range(k):
        j, k = 0, i
        while k < len(text) and text[k] == text[j]:
            j, k = j + 1, k + 1
            z_array[i] += 1

    return z_array


def generate_words(char_set, length):
    for word in product(char_set, repeat=length):
        yield ''.join(c for c in word)


def test_z_algorithm__corner_cases():
    for c in range(1, 4):
        for length in range(1, 11):
            for word in generate_words(ascii_lowercase[:c], length):
                assert brute_force(word) == z_function(word)


def test_z_algorithm__large_cases():
    for c in range(1, 10):
        length = 10**5
        text = ''.join(choice(ascii_lowercase[:c]) for _ in range(length))
        z_array = z_function(text)
        assert z_array[:100] == brute_force(text, 100)
