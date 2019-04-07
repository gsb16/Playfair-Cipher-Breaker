#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unicodedata

# Gerador de chaves
def generateWords(iterator):
    if iterator == 0:
        return [chr(ord('a') + i) for i in range (26)]
    else:
        return [chr(ord('a') + i)+j for i in range (26) for j in generateWords(iterator - 1)]

X = 0

filekeys = open("keys/keys"+str(X), "w+")

for word in generateWords(X-1):
    ok = True
    for c in word:
        if c == 'j':
            ok = False
        if word.count(c) > 1:
            ok = False
    if ok:
        filekeys.write(word + '\n')

# Gerador de dicionário
finput = open("/usr/share/dict/brazilian", "r")
cleandict = open("clean_dict", "w+")

for line in finput:
    for word in line.split():
        word = word.decode('latin1')
        word = unicodedata.normalize('NFKD', word).encode('ASCII', 'ignore')
        word = word.lower().replace('j', 'i')
        cleandict.write(word + '\n')


# Gerador de dicionário de chaves (palavras de 3, 4, 5, 6 letras)
finput = open("clean_dict", "r")
cleandict = open("keysDict", "w+")

for line in finput:
    for word in line.split():
        leng = len(word)
        if leng >= 3 and leng <= 6:
            cleandict.write(word + '\n')
