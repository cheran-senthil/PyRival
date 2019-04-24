import _random


class Random(_random.Random):
    def shuffle(self, x):
        for i in range(len(x) - 1, 0, -1):
            j = int(self.random() * (i + 1))
            x[i], x[j] = x[j], x[i]

    randint = lambda self, a, b: a + int(self.random() * (b - a + 1))
    choice = lambda self, seq: seq[int(self.random() * len(seq))]
    randrange = lambda self, a, b, step=1: a + step * int(
        self.random() * ((b - a + step + [1, -1][step < 0]) // step)
    )


randint = Random().randint
