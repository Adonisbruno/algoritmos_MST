import numpy as np

def lerArquivoToList(file, flag):
    # usando no DIJKSTRA e PRIM
    arr = []
    inp = open(file, flag)
    # ler a linha do arquivo
    for line in inp.readlines():
        # adiciona uma sublista a lista
        arr.append([])
        # separa os elementos nos espacos, a cada espaco, separa...
        for i in line.split():
            # converte para inteiro e adiciona ao final da linha
            arr[-1].append(int(i))
    inp.close()
    return arr


def loadMatrizAdjacencia(inputList, ordem):
    m = np.zeros((ordem, ordem), dtype=int)
    cc = 1
    for i, c in enumerate(inputList):
        for j in range(len(inputList[i])):
            # print(i-1,j+cc-1, arr[i][j])
            m[i - 1][j + cc - 1] = inputList[i][j]
            m[j + cc - 1][i - 1] = inputList[i][j]
        cc += 1
    return m
