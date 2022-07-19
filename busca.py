from profundidade import *

percurso = []
caminho = []
posicao = input("Posição Inicial").upper()
posFinal = input("Posicao Final").upper()
percurso.append(posicao)
caminho.append(posicao)
posAtual(posicao)
while posicao != posFinal:
    #caminho.append(posicao)
    if posicao == 'A':
        print("POSIÇÃO A")
        posAtual(posicao)
        if len(lista[0]) > 0:
            posicao = lista[0][0]
            if posicao == posFinal:
                caminho.append(posicao)
            else:
                percurso.append(posicao)
                caminho.append(posicao)

        else:
            percurso = percurso[:-1]
            posicao = percurso[-1]
            caminho.append(posicao)
    elif posicao == 'B':
        print("POSIÇÃO B")
        posAtual(posicao)
        if len(lista[1]) > 0:
            posicao = lista[1][0]
            if posicao == posFinal:
                caminho.append(posicao)
            else:
                percurso.append(posicao)
                caminho.append(posicao)
        else:
            percurso = percurso[:-1]
            posicao = percurso[-1]
            caminho.append(posicao)
    elif posicao == 'C':
        print("POSIÇÃO C")
        posAtual(posicao)
        if len(lista[2]) > 0:
            posicao = lista[2][0]
            if posicao == posFinal:
                caminho.append(posicao)
            else:
                percurso.append(posicao)
                caminho.append(posicao)
        else:
            percurso = percurso[:-1]
            posicao = percurso[-1]
            caminho.append(posicao)
    elif posicao == 'D':
        print("POSIÇÃO D")
        posAtual(posicao)
        if len(lista[3]) > 0:
            posicao = lista[3][0]
            if posicao == posFinal:
                caminho.append(posicao)
            else:
                percurso.append(posicao)
                caminho.append(posicao)
        else:
            percurso = percurso[:-1]
            posicao = percurso[-1]
            caminho.append(posicao)
    elif posicao == 'E':
        print("POSIÇÃO E")
        posAtual(posicao)
        if len(lista[4]) > 0:
            posicao = lista[4][0]
            if posicao == posFinal:
                caminho.append(posicao)
            else:
                percurso.append(posicao)
                caminho.append(posicao)
        else:
            percurso = percurso[:-1]
            posicao = percurso[-1]
            caminho.append(posicao)
    elif posicao == 'F':
        print("POSIÇÃO F")
        posAtual(posicao)
        if len(lista[5]) > 0:
            posicao = lista[5][0]
            if posicao == posFinal:
                caminho.append(posicao)
            else:
                percurso.append(posicao)
                caminho.append(posicao)
        else:
            percurso = percurso[:-1]
            posicao = percurso[-1]
            caminho.append(posicao)
    elif posicao == 'G':
        print("POSIÇÃO G")
        posAtual(posicao)
        if len(lista[6]) > 0:
            posicao = lista[6][0]
            if posicao == posFinal:
                caminho.append(posicao)
            else:
                percurso.append(posicao)
                caminho.append(posicao)
        else:
            percurso = percurso[:-1]
            posicao = percurso[-1]
            caminho.append(posicao)
    elif posicao == 'H':
        print("POSIÇÃO H")
        posAtual(posicao)
        if len(lista[7]) > 0:
            posicao = lista[7][0]
            if posicao == posFinal:
                caminho.append(posicao)
            else:
                percurso.append(posicao)
                caminho.append(posicao)
        else:
            percurso = percurso[:-1]
            posicao = percurso[-1]
            caminho.append(posicao)
    else:
        print("break")
        break
print("-->".join(caminho))
