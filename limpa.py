inputtext = open("teste.txt", "r")
outtext = open("teste2.txt", "w+")

text = inputtext.read()

text = text.replace(" ", "")

text = text[:200]

outtext.write(text)
