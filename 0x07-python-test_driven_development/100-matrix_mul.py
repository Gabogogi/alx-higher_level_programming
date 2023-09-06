#!/usr/bin/python3
"""This module contains a function that multiplies two matrices."""


def matrix_mul(m_a, m_b):
    """
    Multiply two matrices.

    Args:
        m_a (list of lists): The first matrix.
        m_b (list of lists): The second matrix.

    Returns:
        list of lists: The result of multiplying the two matrices.
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    num_columns_a = 0
    num_rows_b = 0

    if not m_a:
        raise ValueError("m_a can't be empty")

    for row_a in m_a:
        if not isinstance(row_a, list):
            raise TypeError("m_a must be a list of lists")

        if not row_a:
            raise ValueError("m_a can't be empty")

        if len(row_a) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")

        num_columns_a = len(row_a)

        for element in row_a:
            if not isinstance(element, (int, float)):
                raise TypeError("m_a should contain only integers or floats")

    if not m_b:
        raise ValueError("m_b can't be empty")

    for row_b in m_b:
        if not isinstance(row_b, list):
            raise TypeError("m_b must be a list of lists")

        if not row_b:
            raise ValueError("m_b can't be empty")

        if len(row_b) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")

        num_rows_b += 1

        for element in row_b:
            if not isinstance(element, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    if num_columns_a != num_rows_b:
        raise ValueError("m_a and m_b can't be multiplied")

    result_matrix = []

    for row_a in m_a:
        result_row = []
        for low in range(len(m_b[0])):
            result = 0
            for k, column_a in enumerate(row_a):
                result += column_a * m_b[k][low]
            result_row.append(result)
        result_matrix.append(result_row)

    return result_matrix
