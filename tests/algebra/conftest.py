import os

import pytest

DATA_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data")


@pytest.fixture
def phi():
    with open(os.path.join(DATA_DIR, "phi.txt")) as f:
        return [int(i) for i in f.read().split(" ")]


@pytest.fixture
def primes():
    with open(os.path.join(DATA_DIR, "primes.txt")) as f:
        return [int(i) for i in f.read().split(" ")]


@pytest.fixture
def prime_set(primes):
    return set(primes)
