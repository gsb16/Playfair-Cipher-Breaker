#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Cell:
    def __init__(self, val, i, j):
        self.val = val
        self.i = i
        self.j = j

def generateMatrixString(key):
    alphabet = [chr(ord('a') + i) for i in range (26)]
    alphabet.remove('j')
    stri = ""
    for k in key:
        if k not in stri:
            stri += k
    for d in alphabet:
        if d not in key:
            stri += d
    return stri

def generateMatrixDict(grid, stri):
    for i in range(25):
        grid.append(Cell(stri[i], i / 5, i % 5))
    grid = grid.sort(key=lambda x: x.val)

def generateMatrix(matrix, stri):
    for i in range(5):
        for j in range(5):
            matrix[i][j] = stri[i*5 + j]

def getValues(matrix, charList, digram, isCiphing):
    a = 0 if ord(digram[0]) < ord('j') else -1
    b = 0 if ord(digram[1]) < ord('j') else -1
    a += ord(digram[0]) - ord('a')
    b += ord(digram[1]) - ord('a')
    a = charList[a]
    b = charList[b]

    if a.i == b.i:
        return (matrix[a.i][(a.j + (1 * isCiphing)) % 5],
                matrix[a.i][(b.j + (1 * isCiphing)) % 5])
    elif a.j == b.j:
        return (matrix[(a.i + (1 * isCiphing)) % 5][a.j],
                matrix[(b.i + (1 * isCiphing)) % 5][a.j])
    else:
        return (matrix[a.i][b.j],
                matrix[b.i][a.j])
