import string
from itertools import product

from pyrival.strings.z_algorithm import z_function


def brute_force(text):
    z_array = [0] * len(text)

    for i in range(len(text)):
        j, k = 0, i
        while k < len(text) and text[k] == text[j]:
            j, k = j + 1, k + 1
            z_array[i] += 1

    return z_array


def generate_words(char_set, length):
    for word in product(char_set, repeat=length):
        yield ''.join(c for c in word)


def test_z_algorithm():
    for c in range(1, 4):
        for length in range(1, 11):
            for word in generate_words(string.ascii_lowercase[:c], length):
                assert brute_force(word) == z_function(word)
