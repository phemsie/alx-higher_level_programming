#!/usr/bin/python3
""" module defines pascal_triangle method """


def pascal_triangle(n):
    """
       returns a list of lists of integers
       representing the Pascal’s triangle of n
    args:
        n: int of pascal tringle dimension
    """
    triangle = []
    tmp = 0
    if n <= 0:
        return triangle
    for value in range(n):
        List = []
        for i in range(value + 1):
            if i == 0 or i == value:
                List.append(1)
            else:
                tmp = (triangle[value - 1][i - 1] + triangle[value - 1][i])
                List.append(tmp)
        triangle.append(List)
    return triangle


if __name__ == "__main__":
    print(pascal_triangle(5))
