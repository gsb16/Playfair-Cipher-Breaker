#!/usr/bin/env python
# -*- coding: utf-8 -*-

import playfair as pf
import sys

if len(sys.argv) < 3:
    print "requer ao menos 2 parâmetro texto cifrado e chave(s)"

text = open(sys.argv[1], "r")
intertext = text.read()

for key in sys.argv[2:]:
    stringText = pf.generateMatrixString(key)
    charDict = []
    pf.generateMatrixDict(charDict, stringText)
    matrix = [[0 for x in range(5)] for y in range(5)]
    pf.generateMatrix(matrix, stringText)

    exittext = ""
    for i in range(0, len(intertext), 2):
        stringText = intertext[i:i+2]
        if len(stringText) == 0 or '\n' in stringText:
            break
        par = pf.getValues(matrix, charDict, stringText, -1)
        exittext += par[0] + par[1]

    outfile = open("chave-"+key, "w+")
    outfile.write(exittext)
