import os

import pytest

DATA_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data")


@pytest.fixture
def derangements():
    with open(os.path.join(DATA_DIR, "derangements.txt")) as f:
        return [int(i) for i in f.read().split(" ")]


@pytest.fixture
def catalan():
    with open(os.path.join(DATA_DIR, "catalan.txt")) as f:
        return [int(i) for i in f.read().split(" ")]
