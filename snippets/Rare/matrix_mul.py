def matrix_mul(matrix1, matrix2):
    rows, columns, length = len(matrix1), len(matrix2[0]), len(matrix2)
    matrix = [[0] * columns for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            matrix[i][j] = sum(matrix1[i][k] * matrix2[k][j]
                               for k in range(length))
    return matrix
