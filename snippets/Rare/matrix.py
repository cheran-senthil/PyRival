class Matrix(object):
    def __init__(self, m, n, init=True):
        if init:
            self.rows = [[0]*n for x in range(m)]
        else:
            self.rows = []
        self.m = m
        self.n = n

    def __getitem__(self, idx):
        return self.rows[idx]

    def __setitem__(self, idx, item):
        self.rows[idx] = item

    def __str__(self):
        s = '\n'.join([' '.join([str(item) for item in row]) for row in self.rows])
        return s + '\n'

    def transpose(self):
        m, n = self.n, self.m
        mat = Matrix(m, n)
        mat.rows = [list(item) for item in zip(*self.rows)]

        return mat

    def __eq__(self, mat):
        return (mat.rows == self.rows)

    def __add__(self, mat):
        ret = Matrix(self.m, self.n)

        for x in range(self.m):
            row = [sum(item) for item in zip(self.rows[x], mat[x])]
            ret[x] = row

        return ret

    def __sub__(self, mat):
        ret = Matrix(self.m, self.n)

        for x in range(self.m):
            row = [item[0]-item[1] for item in zip(self.rows[x], mat[x])]
            ret[x] = row

        return ret

    def __mul__(self, mat):
        matm, matn = mat.m, mat.n

        mat_t = mat.transpose()
        mulmat = Matrix(self.m, matn)

        for x in range(self.m):
            for y in range(mat_t.m):
                mulmat[x][y] = sum([item[0]*item[1] for item in zip(self.rows[x], mat_t[y])])

        return mulmat

    def __iadd__(self, mat):
        tempmat = self + mat
        self.rows = tempmat.rows[:]
        return self

    def __isub__(self, mat):
        tempmat = self - mat
        self.rows = tempmat.rows[:]
        return self

    def __imul__(self, mat):
        tempmat = self * mat
        self.rows = tempmat.rows[:]
        self.m, self.n = tempmat.getRank()
        return self

    def __pow__(self, power):
        if power == 0:
            return self.makeId(self.m)

        powers = '{0:b}'.format(power)[::-1]

        matrices = [None for _ in powers]
        matrices[0] = self

        for i in range(1, len(powers)):
            matrices[i] = matrices[i - 1] * matrices[i - 1]

        result = None

        for matrix, power in zip(matrices, powers):
            if power == '1':
                if result is None:
                    result = matrix
                else:
                    result = result * matrix

        return result

    @classmethod
    def _makeMatrix(cls, rows):

        m = len(rows)
        n = len(rows[0])
        mat = Matrix(m, n, init=False)
        mat.rows = rows

        return mat

    @classmethod
    def makeZero(cls, m, n):
        rows = [[0]*n for x in range(m)]
        return cls.fromList(rows)

    @classmethod
    def makeId(cls, m):
        rows = [[0]*m for x in range(m)]
        idx = 0

        for row in rows:
            row[idx] = 1
            idx += 1

        return cls.fromList(rows)

    @classmethod
    def fromList(cls, listoflists):
        rows = listoflists[:]
        return cls._makeMatrix(rows)


m = Matrix.fromList([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(m**2)