import os


class ReadNumbers:
    def __init__(self, var=int):
        self.ind = 0
        self.numbers = []

        num, sign = var(0), 1
        for char in os.read(0, os.fstat(0).st_size):
            if char >= 48:
                num = 10 * num + char - 48
            elif char == 45:
                sign = -1
            elif char != 13:
                self.numbers.append(sign * num)
                num, sign = var(0), 1

        if char >= 48:
            self.numbers.append(sign * num)

    def getnum(self):
        self.ind += 1
        return self.numbers[self.ind - 1]


getnum = ReadNumbers().getnum
