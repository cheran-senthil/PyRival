from _random import Random

Random = Random()

random = Random.random


def randrange(start, stop, step=1):
    if step == 1 and stop > start:
        return start + int(random() * (stop - start))

    n = (stop - start + step + [1, -1][step < 0]) // step
    return start + step * int(random() * n)


def shuffle(x):
    for i in range(len(x) - 1, 0, -1):
        j = int(random() * (i + 1))
        x[i], x[j] = x[j], x[i]


randint = lambda a, b: a + int(random() * (b - a + 1))
choice = lambda seq: seq[int(random() * len(seq))]
