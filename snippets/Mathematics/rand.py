from _random import Random

random = Random().random
randint = lambda a, b: a + int(random() * (b - a + 1))


def shuffle(x):
    for i in range(len(x) - 1, 0, -1):
        j = randint(0, i)
        x[i], x[j] = x[j], x[i]
