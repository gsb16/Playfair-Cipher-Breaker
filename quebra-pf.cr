# entrada de dados
chaves = ""
textocifrado = ""

ARGV.each_with_index do |item, index|
    if item == "-d"
        if ARGV.size() > index+1
            chaves = ARGV[index+1]
        end
    end
    if item == "-t"
        if ARGV.size() > index+1
            textocifrado = ARGV[index+1]
        end
    end
end

keys = File.read_lines(chaves.as(String))
texto = File.read(textocifrado.as(String))
# fim entrada de dados

# preparação das informações
sizetexto = texto.size()

ALPHABET = "abcdefghiklmnopqrstuvwxyz"
STRVOGAIS = "a e o"
STRDIGRAMAS = "de ra es do en"
STRTRIGRAMAS = "que ent com est ndo"
# fim preparação das informações

# funções relacionadas a Playfair
def generateMatrixString(key)
    stri = ""

    key.each_char do |char|
        unless stri.includes?(char)
            stri += char
        end
    end

    ALPHABET.each_char do |char|
        unless stri.includes?(char)
            stri += char
        end
    end

    stri
end

def generateMatrixDict(stri)
    arr = Array.new(25){ |i| [stri[i], i/5, i%5]}
    arr.sort{ |x, y| x[0].as(Char) - y[0].as(Char) }

end

def generateMatrix(stri)
    matrix = Array.new(5) { |i| Array.new(5) {|j| stri[i*5 + j]} }
end

def getValues(matrix, charDict, digram)
    a = digram[0] < 'j' ? 0 : -1
    b = digram[1] < 'j' ? 0 : -1

    a = charDict[a + (digram[0] - 'a')]
    b = charDict[b + (digram[1] - 'a')]

    ai = a[1].as(Int32)
    bi = b[1].as(Int32)
    aj = a[2].as(Int32)
    bj = b[2].as(Int32)

    if ai == bi
        return matrix[ai][(aj - 1) % 5] + "" + matrix[ai][(bj - 1) % 5]
    elsif aj == bj
        return matrix[(ai - 1) % 5][aj] + "" + matrix[(bi - 1) % 5][aj]
    else
        return matrix[ai][bj] + "" + matrix[bi][aj]
    end
end
# fim funções relacionadas a Playfair

# inicialização de dados
key = 0
keyscount = keys.size()
myarr = Array.new(5){|i| {-1, "ab"}}
# fim inicialização de dados

# loop principal (executa para cada chave)
while key < keyscount
    # geração da playfar para chave da rodada
    mystring = generateMatrixString(keys[key])
    mydict = generateMatrixDict(mystring)
    mymatrix = generateMatrix(mystring)
    # fim geração da playfar para chave da rodada

    # decifra texto com chave da rodada
    i = 0
    textoclaro = ""
    tam  = sizetexto - 1
    while i < tam
        textoclaro += getValues(mymatrix, mydict, texto[i, 2])
        i += 2
    end
    # fim decifra texto com chave da rodada

    # calculo do score da chave atual
    vogais = 0
    digramas = 0
    trigramas = 0
    tam = sizetexto

    i = 0
    while i < tam
        if STRVOGAIS.includes?(textoclaro[i, 1])
            vogais += 1
        end
        if STRDIGRAMAS.includes?(textoclaro[i, 2])
            digramas += 1
        end
        if STRTRIGRAMAS.includes?(textoclaro[i, 3])
            trigramas += 1
        end
        i += 1
    end

    total = trigramas + digramas + vogais
    # fim calculo do score da chave atual

    # atualização das top 5 chaves
    menor = myarr.reduce{ |acc, i| acc[0] > i[0] ? i : acc}
    if menor[0] < total
        myarr[myarr.index(menor).as(Int32)] = {total, keys[key]}
    end
    # fim atualização das top 5 chaves

    key += 1
end
# fim loop principal (executa para cada chave)

# impressão das chaves encontradas
myarr.each do |key|
    print " " + key[1]
end

puts ""
# fim impressão das chaves encontradas
