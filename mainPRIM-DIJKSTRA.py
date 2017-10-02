from auxiliar import lerArquivoToList, loadMatrizAdjacencia
import numpy as np
import sys

# foi criada uma classe Grafo para facilitar a implementação do PRIM e DIJKSTRA
class Grafo():
    # função de inicialização do grafo
    def __init__(self, vertices):
        self.V = vertices
        self.grafo = np.zeros((vertices, vertices), dtype=np.int)

    # Uma funcao para imprimir o MST_PRIM construido armazenado no pred[]
    def printMST_PRIM(self, pred):
        custo = 0
        print("(v[i]-pred[i])  Custo")
        for i in range(1, self.V):
            print(" ", i, "-", pred[i], "\t", self.grafo[i][pred[i]])
            custo += self.grafo[i][pred[i]]
        print("\n\nCusto Total: ", custo)

    # funcao para imprimir a saida do DIJKSTRA
    def printDIJKSTRA(self, pred, d):
        print("(v[i]-pred[i])  Distancia da Origem")
        for i in range(1, self.V):
            print(i, "-", pred[i], "\t\t", d[i])

    # Funcao para encontrar o vertice com valor de distancia minima
    def EXTRACT_MIN(self, chave, mstSet):
        # Inicializa minimo com infinito
        min_index = 0
        min = np.inf
        for v in range(self.V):
            if chave[v] < min and mstSet[v] == False:
                min = chave[v]
                min_index = v
        return min_index

    # Funcao para construir MST para um grafico representado usando
    # representacao da matriz de adjacencia
    def MST_PRIM(self):

        # Chave utilizados para escolher a ponta minima em corte
        chave = [np.inf] * self.V
        # mstSet[v] eh falso para vertices ainda nao incluidos no MST
        mstSet = [False] * self.V
        # Array para armazenar MST
        pred = [None] * self.V
        # Faca a chave 0 para que este vertice seja escolhido como primeiro vertice
        chave[0] = 0
        # Primeiro nodo sera a raiz sempre
        pred[0] = -1

        for cout in range(self.V):
            # Escolha o vertice de distancia minima do conjunto de vertices nao ainda processado.
            u = self.EXTRACT_MIN(chave, mstSet)
            # Coloque o vertice da distancia minima na arvore
            mstSet[u] = True

            for v in range(self.V):
                # Atualize a chave somente se o grafo[u][v] for menor do que a chave[v]
                if self.grafo[u][v] > 0 and mstSet[v] == False and self.grafo[u][v] < chave[v]:
                    chave[v] = self.grafo[u][v]
                    pred[v] = u

        return pred

    def DIJKSTRA(self):

        # distancias
        d = [np.inf] * self.V
        # Array para armazenar MST
        pred = [None] * self.V
        # mstSet[v] eh falso para vertices ainda nao incluidos no MST
        mstSet = [False] * self.V
        # Faca a chave 0 para que este vertice seja escolhido como primeiro vertice
        d[0] = 0

        for i in range(self.V):
            # Escolha o vertice de distancia minima do conjunto de vertices nao ainda processado.
            u = self.EXTRACT_MIN(d, mstSet)
            # Coloque o vertice da distancia minima na arvore
            mstSet[u] = True

            for v in range(self.V):
                # relaxamento do DIJKSTRA
                if self.grafo[u][v] > 0 and mstSet[v] == False and d[v] > d[u] + self.grafo[u][v]:
                    d[v] = d[u] + self.grafo[u][v]
                    pred[v] = u
        return d, pred

def main():
    global vetor, opt
    if len(sys.argv) < 3:
        print("python mainPRIM-DIJKSTRA.py instancias_Dijkstra_e_PRIM/dij10.txt PRIM | DIJK > saidaPD.txt")
        print("Exemplo: python mainPRIM-DIJKSTRA.py instancias_Dijkstra_e_PRIM/dij10.txt DIJK > saidaPD.txt")
        sys.exit(-1)
    try:
        # ler arquivo para uma lista
        vetor = lerArquivoToList(sys.argv[1], "r")
        opt = sys.argv[2]
    except ValueError:
        print("valores invalidos")
        sys.exit(-1)


if __name__ == "__main__":
    main()

    # retira o primeiro elemento que é a ordem da matriz
    ordem = vetor[0].pop()
    # com os demais elementos carrega na matriz de adjacencias
    matrixAdj = loadMatrizAdjacencia(vetor, ordem)

    if opt == 'PRIM':
        g = Grafo(ordem)
        g.grafo = matrixAdj
        pred = g.MST_PRIM()
        g.printMST_PRIM(pred)

    if opt == 'DIJK':
        g = Grafo(ordem)
        g.grafo = matrixAdj
        d, pred = g.DIJKSTRA()
        g.printDIJKSTRA(pred, d)

