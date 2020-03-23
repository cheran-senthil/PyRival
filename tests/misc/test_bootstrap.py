import random

import pyrival.misc


def test_bootstrap():
    @pyrival.misc.bootstrap
    def func(n):
        if n:
            yield (yield func(n - 1)) + n
        yield 0

    assert func(100000) == 5000050000
