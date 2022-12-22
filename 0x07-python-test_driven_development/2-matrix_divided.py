#!/usr/bin/python3
""" a module for a function that divides all elements of a matrix. """


def matrix_divided(matrix, div):
    """ function to div all elements of a matrix
    Args:
        matrix: list of lists of type int or float
        div: number of type int or float but not zero
    Returns:
        list of lists type int or float
    Raises:
        TypeError: matrix is not of valid format
        ZeroDivisionError: division by zero
    """

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list) or not matrix:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")
    if not isinstance(matrix[0], list) or not matrix[0]:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")

    size = len(matrix[0])
    matx = [[0 for j in range(size)] for i in range(len(matrix))]
    for i in range(len(matrix)):
        if type(matrix[i]) is not list:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        if size != len(matrix[i]):
            raise TypeError("Each row of the matrix must have the same size")
        for j in range(len(matrix[i])):
            if type(matrix[i][j]) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")
            matx[i][j] = matrix[i][j] / div
            matx[i][j] = round(matx[i][j], 2)

    return matx

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
