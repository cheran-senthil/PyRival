transpose = lambda mat: [list(item) for item in zip(*mat)]


mat_add = lambda *mat: [[sum(elements) for elements in zip(*row)] for row in zip(*mat)]


mat_sub = lambda mat1, mat2: [[i - j for i, j in zip(*row)] for row in zip(mat1, mat2)]


mat_mul = lambda mat1, mat2: [[sum(i * j for i, j in zip(row, col)) for col in transpose(mat2)] for row in mat1]


def mat_pow(mat, power):
    result = [[1 if i == j else 0 for j in range(len(mat))] for i in range(len(mat))]

    if power == 0:
        return result

    powers = '{0:b}'.format(power)[::-1]

    matrices = [None for _ in powers]
    matrices[0] = mat

    for i in range(1, len(powers)):
        matrices[i] = mat_mul(matrices[i - 1], matrices[i - 1])

    for matrix, power in zip(matrices, powers):
        if power == '1':
            result = mat_mul(result, matrix)

    return result
