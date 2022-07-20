import re
lista = ['BG', 'ACH', 'BF', 'EH', 'DF', 'CE', 'A', 'BD']
#lista = ['BD', 'AC', 'B', 'A']


def posAtual(posicao):
    if posicao == 'A':
        for i in range(len(lista)):
            item1 = re.sub('A', '', lista[i])
            lista[i] = item1
        for i in lista[0]:
            x = lista[0]
            for j in range(len(lista)):
                item = re.sub(i, '', lista[j])
                lista[j] = item
                lista[0] = x
    elif posicao == 'B':
        for i in range(len(lista)):
            item1 = re.sub('B', '', lista[i])
            lista[i] = item1
        for i in lista[1]:
            x = lista[1]
            for j in range(len(lista)):
                item = re.sub(i, '', lista[j])
                lista[j] = item
                lista[1] = x
    elif posicao == 'C':
        for i in range(len(lista)):
            item1 = re.sub('C', '', lista[i])
            lista[i] = item1
        for i in lista[2]:
            x = lista[2]
            for j in range(len(lista)):
                item = re.sub(i, '', lista[j])
                lista[j] = item
                lista[2] = x
    elif posicao == 'D':
        for i in range(len(lista)):
            item1 = re.sub('D', '', lista[i])
            lista[i] = item1
        for i in lista[3]:
            x = lista[3]
            for j in range(len(lista)):
                item = re.sub(i, '', lista[j])
                lista[j] = item
                lista[3] = x
    elif posicao == 'E':
        for i in range(len(lista)):
            item1 = re.sub('E', '', lista[i])
            lista[i] = item1
        for i in lista[4]:
            x = lista[4]
            for j in range(len(lista)):
                item = re.sub(i, '', lista[j])
                lista[j] = item
                lista[4] = x
    elif posicao == 'F':
        for i in range(len(lista)):
            item1 = re.sub('F', '', lista[i])
            lista[i] = item1
        for i in lista[5]:
            x = lista[5]
            for j in range(len(lista)):
                item = re.sub(i, '', lista[j])
                lista[j] = item
                lista[5] = x
    elif posicao == 'G':
        for i in range(len(lista)):
            item1 = re.sub('G', '', lista[i])
            lista[i] = item1
        for i in lista[6]:
            x = lista[6]
            for j in range(len(lista)):
                item = re.sub(i, '', lista[j])
                lista[j] = item
                lista[6] = x

    elif posicao == 'H':
        for i in range(len(lista)):
            item1 = re.sub('H', '', lista[i])
            lista[i] = item1
        for i in lista[7]:
            x = lista[7]
            for j in range(len(lista)):
                item = re.sub(i, '', lista[j])
                lista[j] = item
                lista[7] = x

"""
posAtual('E')
print(lista)
posAtual('D')
print(lista)
posAtual('H')
print(lista)
posAtual('B')
print(lista)
posAtual('A')
print(lista)
posAtual('G')
print(lista)
posAtual('A')
print(lista)
posAtual('B')
print(lista)
posAtual('C')
print(lista)
posAtual('B')
print(lista)
posAtual('H')
print(lista)
posAtual('D')
print(lista)
posAtual('E')
print(lista)
posAtual('F')
print(lista)
"""