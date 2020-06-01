import random

import pyrival.algebra


def test_discrete_log__corner_cases(limit=100):
    for a in range(limit):
        for b in range(limit):
            for m in range(1, limit):
                x = pyrival.algebra.discrete_log(a, b, m)
                if x is not None:
                    assert pow(a, x, m) == b

    for a in range(limit):
        for m in range(1, limit):
            uniques = set()
            processed = set()
            for x in range(limit):
                b = pow(a, x, m)
                ans = pyrival.algebra.discrete_log(a, b, m)
                assert pow(a, ans, m) == b
                assert x == ans or ans in processed
                processed.add(ans)
                uniques.add(b)

            for b in set(range(limit)) - uniques:
                x = pyrival.algebra.discrete_log(a, b, m)
                assert x is None


def test_discrete_log__random_cases(trials=200):
    random.seed(666)

    for _ in range(trials):
        m = random.randint(0, 10**9)
        a = random.randint(0, m)
        x = random.randint(0, 10**9)
        b = pow(a, x, m)

        assert pow(a, pyrival.algebra.discrete_log(a, b, m), m) == b
