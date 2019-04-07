#!/usr/bin/env python
# -*- coding: utf-8 -*-

import playfair as pf
import unicodedata
import string
import sys

if len(sys.argv) < 3:
    print "requer 2 parâmetros, chave e arquivo de entrada"
    exit(-1)

key = sys.argv[1]
inputtext = open(sys.argv[2], "r")

# playfair setup
stringText = pf.generateMatrixString(key)
charDict = []
pf.generateMatrixDict(charDict, stringText)
matrix = [[0 for x in range(5)] for y in range(5)]
pf.generateMatrix(matrix, stringText)
# fim playfair setup

# tratamento do texto aberto
text = ""
intertext = ""
for line in inputtext:
    for word in line.split():
        word = word.translate(None, string.punctuation)
        word = word.decode('latin1')
        word = unicodedata.normalize('NFKD', word).encode('ASCII', 'ignore')
        word = word.lower().replace('j', 'i')
        word = word.replace(' ', '')
        text += word

text = text.translate(None, string.digits)

for i in range(0, len(text)-1):
    intertext += text[i]
    if text[i] == text[i+1]:
        intertext += 'x'
intertext += text[len(text)-1]

if len(intertext) % 2 != 0:
    intertext += 'x'
# fim tratamento texto abertos

# cifragem propriamente dita
exittext = ""
for i in range(0, len(intertext), 2):
    stringText = intertext[i:i+2]
    if len(stringText) == 0 or '\n' in stringText:
        break
    par = pf.getValues(matrix, charDict, stringText, 1)
    exittext += par[0] + par[1]
# fim cifragem propriamente dita

if len(sys.argv) == 4:
    outputtext = open(sys.argv[3], "w+")
    outputtext.write(exittext)
else:
    print exittext
