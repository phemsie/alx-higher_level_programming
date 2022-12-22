#!/usr/bin/python3
""" a module for a function that multiplies 2 matrices """

import numpy


def lazy_matrix_mul(m_a, m_b):
    """ function that multiplies 2 matrices
    Args:
        m_a: the first matrice
        m_b: the second matrice
    Returns:
        matrice: a product of m_a * m_b
    Raises:
        TypeError: If m_a or m_b are not lists
        TypeError: If m_a or m_b are not lists of lists
        TypeError: If m_a or m_b Contain not int nor float
        TypeError: If m_a or m_b are not rectangular
        ValueError: If m_a or m_b are empty lists or matrice
        ValueError: If m_a or m_b can't be multiplied
    """
    m_a_empty = False
    m_b_empty = False
    m_a_scalar = False
    m_b_scalar = False
    m_a_notrect = False
    m_b_notrect = False
    m_a_notnum = False
    m_b_notnum = False
    for row in m_a:
        if not isinstance(row, list):
            m_a_scalar = True
        if len(row) != len(m_a[0]):
            m_a_notrect = True
        for num in row:
            if not isinstance(num, (int, float)):
                m_a_notnum = True
    for row in m_b:
        if not isinstance(row, list):
            m_b_scalar = True
        if len(row) != len(m_b[0]):
            m_b_notrect = True
        for num in row:
            if not isinstance(num, (int, float)):
                m_b_notnum = True
    if m_a_scalar:
        raise TypeError("scalar operands are not allowed for m_")
    if m_b_scalar:
        raise TypeError("scalar operands are not allowed for m_")
    if m_a_notnum:
        raise TypeError("m_ contains invalid datatype for einsum")
    if m_b_notnum:
        raise TypeError("m_ contains invalid datatype for einsum")
    if m_a_notrect:
        raise TypeError("array element has unmatched sequence sizes")
    if m_b_notrect:
        raise TypeError("array element has unmatched sequence sizes")
    return numpy.matrix(m_a) * numpy.matrix(m_b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/101-lazy_matrix_mul.txt")
