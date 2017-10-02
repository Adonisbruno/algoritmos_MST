import numpy as np

def lerArquivoToList(file, flag):
    # Funcao ler arquivo linha a linha e converte em uma lista
    # file := local e nome do arquivo ".../dij10.txt"
    #  flag := modo de leitura "r"

    # array de retorno
    arr = []
    inp = open(file, flag)
    # ler a linha do arquivo
    for line in inp.readlines():
        # adiciona uma sublista a lista
        arr.append([])
        # separa os elementos nos espacos
        for i in line.split():
            # converte valor para inteiro e adiciona ao final
            arr[-1].append(int(i))
    inp.close()
    return arr


def loadMatrizAdjacencia(inputList, ordem):
    # inputList := eh a lista de saida da funcao "lerArquivoToList"
    # ordem := primeiro elemento da lista de saida de "lerArquivoToList" (dimensao da matrix)
    
    # array de saida
    m = np.zeros((ordem, ordem), dtype=int)
    cc = 1
    # varre a lista de entrada copiando os elementos
    # para triangulo superior e inferior da matriz de respecitva ordem
    for i, c in enumerate(inputList):
        for j in range(len(inputList[i])):
            # print(i-1,j+cc-1, arr[i][j])
            m[i - 1][j + cc - 1] = inputList[i][j]
            m[j + cc - 1][i - 1] = inputList[i][j]
        cc += 1
    return m
