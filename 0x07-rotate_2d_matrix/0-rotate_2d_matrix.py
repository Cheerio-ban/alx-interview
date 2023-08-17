#!/usr/bin/python3
"""Rotating matrices given"""


def rotate_2d_matrix(matrix):
    """Rotating 2d matrices"""
    column = len(matrix[0])
    columns = []
    for i in range(column):
        col = []
        for r in matrix:
            col.append(r[i])
        col.reverse()
        columns.append(col)
    matrix.clear()
    for col in columns:
        matrix.append(col)
