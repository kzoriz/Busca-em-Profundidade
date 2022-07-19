from profundidade import *

#print(lista)
percurso = []
caminho = []
posicao = input("Posição Inicial").upper()
posFinal = input("Posicao Final").upper()
print(posicao)
percurso.append(posicao)
caminho.append(posicao)
posAtual(posicao)
while posicao != posFinal:
    #caminho.append(posicao)
    if posicao == 'A':
        posAtual(posicao)
        print("POSIÇÃO A")
        print(lista)
        if len(lista[0]) > 0:
            posicao = lista[0][0]
            if posicao == posFinal:
                caminho.append(posicao)
                break
            percurso.append(posicao)
            caminho.append(posicao)

        else:
            print(percurso)
            percurso = percurso[:-1]
            print(percurso)
            posicao = percurso[-1]
            caminho.append(posicao)
            #percurso.append(posicao)
    elif posicao == 'B':
        print("POSIÇÃO B")
        posAtual(posicao)
        print(lista)
        if len(lista[1]) > 0:
            posicao = lista[1][0]
            if posicao == posFinal:
                caminho.append(posicao)
            else:
                percurso.append(posicao)
                caminho.append(posicao)
        else:
            percurso = percurso[:-1]
            print("percurso B")
            print(percurso)
            posicao = percurso[-1]
            caminho.append(posicao)
            #percurso.append(posicao)
    elif posicao == 'C':
        print("POSIÇÃO C")
        posAtual(posicao)
        print(lista)
        if len(lista[2]) > 0:
            posicao = lista[2][0]
            if posicao == posFinal:
                caminho.append(posicao)
            percurso.append(posicao)
            caminho.append(posicao)
        else:
            print(percurso)
            percurso = percurso[:-1]
            print("percurso C")
            print(percurso)
            posicao = percurso[-1]
            caminho.append(posicao)
            #percurso.append(posicao)
            #break
    elif posicao == 'D':
        print("POSIÇÃO D")
        if len(lista[3]) > 0:
            percurso.append(posicao)
            posicao = lista[3][0]
            if posicao == posFinal:
                caminho.append(posicao)
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
#percurso.append(posicao)
print("caminho")
print(caminho)
print("lista")
print(lista)
print("posição")
print(posicao)
