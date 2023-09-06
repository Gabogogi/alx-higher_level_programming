#!/usr/bin/python3
def matrix_divided(matrix, div):
    result = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    for outer_list in matrix:
        for item in outer_list:
            if not isinstance(item, (int, float)):
                raise TypeError("matrix must be a matrix of integers/floats")
    first_row = len(matrix[0])
    for row in matrix:
        if len(row) != first_row:
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result[i][j] = "{:.2f}".format(matrix[i][j] / div)

    return result
