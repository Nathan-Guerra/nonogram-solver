#!/bin/python3

import math
import os
import random
import re
import sys


def solver(h, v):
    print()
    # print(v)
    # print(h)
    fillable = [[None] * len(h)] * len(v)
    m, n, hPost, vPos = 0, 0, 0, 0

    # for n in range(vSize):
    #     for m in range(hSize):
    #         fillable[n][m] = '?'

    # filling rows

    while m < len(h):
        hOffset = len(fillable[m]) - (sum(h[m]) + len(h[m]) - 1)
        maxH = max(h[m])

        # row is completely empty
        if hOffset == len(fillable[m]):
            for i in range(len(fillable[m])):
                fillable[m][i] = 'x'

        # row is completely filled
        if not hOffset:
            spaces = h[m]
            for s in spaces:
                #TODO: terminar de preencher a linha com a quantidade certa
                pass

    return fillable


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lines = input().rstrip().split()
    vSize = int(lines[0])
    hSize = int(lines[1])
    h, v = list(), list()

    for n in range(hSize):
        h.append(list(map(int, input().rstrip().split())))

    for m in range(vSize):
        v.append(list(map(int, input().rstrip().split())))

    response = solver(h, v)
    for n in range(len(response)):
        for m in range(len(response[n])):
            print(response[n][m], end='')
        print()

    # fptr.write(str(total) + '\n')

    # fptr.close()
