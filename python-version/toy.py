#!/usr/bin/env python
# -*- coding: utf-8 -*-

import playfair as pf
import trie

# print "construindo o dicionario..."
# # cria TRIE baseada no dicionario
# tree = trie.Tree()
# finput = open("clean_dict", "r")
# for line in finput:
#     tree.addString(line[:-1])
# print "dicionario construido"

keys = open("keys/keysX", "r")

strVogais = "a e o"
strDigramas = "de ra es do en"
strTrigramas = "que ent com est ndo"

score = [("a", -1), ("a", -1), ("a", -1), ("a", -1), ("a", -1)]

print "testando chaves..."
for line in keys:
    line = line[:-1]
    stringText = pf.generateMatrixString(line)

    charDict = []
    pf.generateMatrixDict(charDict, stringText)

    matrix = [[0 for x in range(5)] for y in range(5)]
    pf.generateMatrix(matrix, stringText)

    fileinput = open("textos/cifrado", "r")

    opened = ""
    counter = 0

    while True:
        stringText = fileinput.read(2)
        if len(stringText) == 0 or '\n' in stringText:
            break
        par = pf.getValues(matrix, charDict, stringText, -1)
        opened += par[0] + par[1]

    vogais = 0
    digramas = 0
    trigramas = 0

    for i in range(len(opened)):
        if opened[i] in strVogais:
            vogais += 1
        if opened[i:i+2] in strDigramas:
            if i < len(opened) - 2:
                digramas += 1
        if opened[i:i+3] in strTrigramas:
            if i < len(opened) - 3:
                trigramas += 1

    total = vogais + digramas + trigramas

    menor = score[0]  
    for s in score:
        menor = s if s[1] < menor[1] else menor

    if menor[1] < total:
        score.remove(menor)
        score.append((line, total))
        
print "chaves testadas"

for s in score:
    print s[0], " -> ", s[1]
