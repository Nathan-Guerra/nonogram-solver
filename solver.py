#!/bin/python3

import math
import numpy as np
import os
import random
import re
import sys


def solver(row, col):
    nonogram = np.zeros((len(row), len(col)))
    print()
    for i in range(len(row)):
        maxFillable = sum(row[i]) + len(row[i]) - 1
        if maxFillable == nonogram[i].size :
            nonogram=fillRow(i, row[i], nonogram)
        elif maxFillable == 0 :
            nonogram=fillEmptyRow(i, nonogram)
        else:
            nonogram=fillRowWithOffset(i, row[i], nonogram[i].size-maxFillable, nonogram)

    return nonogram


def fillRowWithOffset(index, values, offset, board) :
    toPlace = 0
    for i in values:
        aux = offset
        for j in range(i):
            if aux > 0:
                aux -=1
            else:
                board[index][toPlace] = 1
            toPlace += 1
        # gap between two chains
        toPlace += 1
    return board

def fillEmptyRow(index, board):
    for i in range(board[index].size) :
        board[index][i] = -1
    return board

def fillRow(index, values, board):
    toPlace=0
    for i in values:
        for j in range(i):
            board[index][toPlace]=1
            toPlace += 1
        # gap between two chains
        toPlace += 1
    return board


if __name__ == '__main__':
    lines=input().rstrip().split()
    colSize=int(lines[0])
    rowSize=int(lines[1])
    row, col=list(), list()

    for n in range(rowSize):
        row.append(list(map(int, input().rstrip().split())))

    for m in range(colSize):
        col.append(list(map(int, input().rstrip().split())))

    response=solver(row, col)

    for n in range(len(response)):
        for m in range(len(response[n])):
            print(response[n][m], ' ', end='')
        print()
