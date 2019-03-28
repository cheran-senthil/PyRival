from _random import Random

random = Random().random
randint = lambda a, b: a + int(random() * (b - a + 1))
