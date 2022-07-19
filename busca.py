from profundidade import *

#print(lista)
percurso = []
percurso2 = []
posicao = input("Posição Inicial").upper()
posFinal = input("Posicao Final").upper()
posAtual(posicao)
while posicao != posFinal:
    if posicao == 'A':
        print("POSIÇÃO A")
        if len(lista[0]) > 0:
            percurso.append(posicao)
            posicao = lista[0][0]
            posAtual(posicao)
            # print(lista)
            print(percurso)
        else:
            print(percurso)
            percurso2 = percurso.copy()
            posicao = percurso2[-1]
            percurso.append(posicao)
    elif posicao == 'B':
        print("POSIÇÃO B")
        if len(lista[1]) > 0:
            percurso.append(posicao)
            posicao = lista[1][0]
            posAtual(posicao)
            #print(lista)
            print(percurso)
        else:
            percurso.append(posicao)
            print(percurso)
            print(posicao)
            percurso2 = percurso.copy()
            print(percurso2)
            posicao = percurso2[-2]
            print(posicao)
            #percurso.append(posicao)
            print(percurso)

    elif posicao == 'C':
        print("POSIÇÃO C")
        if len(lista[2]) > 0:
            percurso.append(posicao)
            posicao = lista[2][0]
            posAtual(posicao)
           #print(lista)
            print(percurso)
        else:
            print(percurso)
            percurso2 = percurso[-1]
            posicao = percurso2[-1]
            percurso.append(posicao)
    elif posicao == 'D':
        print("POSIÇÃO D")
        if len(lista[3]) > 0:
            percurso.append(posicao)
            posicao = lista[3][0]
            posAtual(posicao)
        else:
            percurso = percurso[-1]
            posicao = percurso[-1]
    elif posicao == 'E':
        print("POSIÇÃO E")
        if len(lista[4]) > 0:
            percurso.append(posicao)
            posicao = lista[4][0]
            posAtual(posicao)
        else:
            percurso = percurso[-1]
            posicao = percurso[-1]
    elif posicao == 'F':
        print("POSIÇÃO F")
        if len(lista[5]) > 0:
            percurso.append(posicao)
            posicao = lista[5][0]
            posAtual(posicao)
        else:
            percurso = percurso[:-1]
            posicao = percurso[-1]
    elif posicao == 'G':
        print("POSIÇÃO G")
        if len(lista[6]) > 0:
            percurso.append(posicao)
            posicao = lista[6][0]
            posAtual(posicao)
        else:
            percurso = percurso[:-1]
            posicao = percurso[-1]
    elif posicao == 'H':
        print("POSIÇÃO H")
        percurso.append(posicao)
        posicao = lista[7][0]
        posAtual(posicao)
    else:
        print("break")
        break
percurso.append(posicao)
print(percurso)
