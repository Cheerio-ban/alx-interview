#!/usr/bin/python3

"""
This module contains a function that implements
the pascal's triangle using 2D lists.
"""


def pascal_triangle(n):
    """
    A function that returns a pascal triangle of any size in its parameter.

    Approach:
        - Initially create an array containing the first two element of the
          pascal's triangle.
        - Take the last element in the array, loop through it and
          create the next element by adding a 1 initially to an
          empty array then adding each element plus the ele-
          ment before it to the new array then add a 1 at the end.
        - Add this new array to the previous array containing the pascal's
          elements.
        - repeat!
    """
    if n <= 0:
        return []

    # Initial pascal's triangle array
    triangle = [[1], [1, 1]]
    count = 2

    # Loop to the number of element needed by the User.
    while count < n:

        # Gets the last element in the pascal's triangle array
        last_elem = triangle[-1]
        temp = []

        # loops over the last element.
        for i in range(len(last_elem)):
            if i == 0:
                temp.append(1)
            else:
                temp.append(last_elem[i] + last_elem[i - 1])
        temp.append(1)
        triangle.append(temp)
        count += 1

    return triangle
