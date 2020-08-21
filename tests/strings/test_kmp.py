import random

from pyrival.kmp import *


def brute_force_match(s, pat):
    idx = []

    for i in range(len(s) - len(pat) + 1):
        found = True
        for j in range(len(pat)):
            found = found and (s[i + j] == pat[j])
        if found:
            idx.append(i)

    return idx


def test_match():
    for _ in range(10000):
        s_len = random.randint(1, 50)
        pat_len = random.randint(1, s_len)

        s = [random.randint(0, 10) for _ in range(s_len)]
        pat = [random.randint(0, 10) for _ in range(pat_len)]

        assert match(s, pat) == brute_force_match(s, pat)


def test_string_find():
    for _ in range(10000):
        s_len = random.randint(1, 50)
        pat_len = random.randint(1, s_len)

        s = [random.randint(0, 10) for _ in range(s_len)]
        pat = [random.randint(0, 10) for _ in range(pat_len)]

        assert string_find(s, pat) == (brute_force_match(s, pat) != [])
