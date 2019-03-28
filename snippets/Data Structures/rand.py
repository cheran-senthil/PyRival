from _random import Random


class random():
    random = Random().random

    @classmethod
    def randint(cls, a, b):
        return a + int(cls.random() * (b - a + 1))

    @classmethod
    def shuffle(cls, x):
        for i in range(len(x) - 1, 0, -1):
            j = cls.randint(0, i)
            x[i], x[j] = x[j], x[i]
