#!/usr/bin/env python
# -*- coding: utf-8 -*-

def indexFromChar(a):
    b = 0 if ord(a) < ord('j') else -1
    b += ord(a) - ord('a')
    return b

class Tree:
    def __init__(self):
        self.root = None

    def addString(self, sta):
        if self.root == None:
            self.root = Node()
        self.root.addString(sta)

    def searchString(self, sts):
        return self.root.searchString(sts)

class Node:
    def __init__(self):
        self.keys = None

    def addString(self, sta):
        index = indexFromChar(sta[0])
        if self.keys == None:
            self.keys = [[0, None] for i in range(25)]

        if len(sta) > 1:
            if self.keys[index][1] == None:
                self.keys[index][1] = Node()
            self.keys[index][1].addString(sta[1:])
        else:
            self.keys[index][0] = 1

    def searchString(self, sts):
        index = indexFromChar(sts[0])
        if self.keys == None:
            return False
        elif len(sts) > 1:
            if self.keys[index][1] != None:
                return self.keys[index][1].searchString(sts[1:])
            else:
                return False
        elif self.keys[index][0] == 0:
            return False
        else:
            return True
