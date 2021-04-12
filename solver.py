#!/bin/python3

import math
import numpy as np
import os
import random
import re
import sys


def solver(row, col):
    nonogram = np.zeros((len(row), len(col)))

    for i in range(len(row)):
        white_spaces = len(row[i]) - 1
        fillable_spaces = sum(row[i])
        col_val = row[i]
        max_fillable = fillable_spaces + white_spaces
        offset = nonogram[i].size - max_fillable

        if max_fillable == nonogram[i].size:
            nonogram = fillRow(i, col_val, nonogram)
        elif max_fillable == 0:
            nonogram = fillEmptyRow(i, nonogram)
        else:
            nonogram = fillRowWithOffset(
                i, col_val, offset, nonogram)

    return nonogram


def fillRowWithOffset(row, col_val, offset, board):
    col = 0
    for i in col_val:
        cur_offset = offset

        for j in range(i):
            if cur_offset > 0:
                cur_offset -= 1
                col += 1
                continue

            board[row][col] = 1
            col += 1

        col += 1
    return board


def fillEmptyRow(row, board):
    row_size = board[row].size

    for i in range(row_size):
        board[row][i] = -1

    return board


def fillRow(row, col_values, board):
    col = 0
    row_size = board[row].size

    for i in col_values:
        for j in range(i):
            board[row][col] = 1
            col += 1

        if col < row_size - 1:
            board[row][col] = -1

        col += 1

    return board


if __name__ == '__main__':
    lines = input().rstrip().split()
    row_size = int(lines[0])
    col_size = int(lines[1])
    row, col = list(), list()

    for m in range(row_size):
        row.append(list(map(int, input().rstrip().split())))

    for n in range(col_size):
        col.append(list(map(int, input().rstrip().split())))

    response = solver(row, col)

    for n in range(len(response)):
        for m in range(len(response[n])):
            print(response[n][m], ' ', end='')
        print()
