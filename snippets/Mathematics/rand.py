from _random import Random

Random = Random()
Random.seed()

randint = lambda a, b: a + int(Random.random() * (b - a + 1))


def shuffle(x):
    for i in range(len(x) - 1, 0, -1):
        j = randint(0, i)
        x[i], x[j] = x[j], x[i]
