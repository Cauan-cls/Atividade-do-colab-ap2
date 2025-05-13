# Maior distância no grafo:

# Tempo: O(n * (n + m)) onde n é o número de vértices e m é o número de arestas (em matriz de adjacência, m ≈ n²), então ≈ O(n³).

# Espaço: O(n) para distâncias e filas.

def maior_distancia(grafo):
    def bfs(origem):
        visitado = []
        distancias = []
        fila = []

        for _ in range(len(grafo)):
            visitado.append(False)
            distancias.append(-1)

        fila.append(origem)
        visitado[origem] = True
        distancias[origem] = 0

        for i in range(len(fila)):
            atual = fila[i]
            for vizinho in range(len(grafo)):
                if grafo[atual][vizinho] == 1 and not visitado[vizinho]:
                    fila.append(vizinho)
                    visitado[vizinho] = True
                    distancias[vizinho] = distancias[atual] + 1

        max_dist = 0
        for d in distancias:
            if d > max_dist:
                max_dist = d
        return max_dist

    maximo = 0  # Corrigido o nível de indentação
    for i in range(len(grafo)):  # Corrigido o nível de indentação
        dist = bfs(i)
        if dist > maximo:
            maximo = dist
    return maximo

# Grafos de teste
grafo_matriz1 = [[0, 1, 1, 0, 0, 0],
                 [1, 0, 1, 1, 0, 1],
                 [1, 1, 0, 1, 1, 0],
                 [0, 1, 1, 0, 1, 1],
                 [0, 0, 1, 1, 0, 1],
                 [0, 1, 0, 1, 1, 0]]

grafo_matriz2 = [[0, 1, 0, 0, 0, 0],
                 [1, 0, 1, 1, 0, 1],
                 [0, 1, 0, 0, 0, 0],
                 [0, 1, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 1],
                 [0, 1, 0, 0, 1, 0]]

grafo_matriz3 = [[0, 1, 0, 0, 0, 0],
                 [1, 0, 1, 0, 0, 0],
                 [0, 1, 0, 1, 0, 0],
                 [0, 0, 1, 0, 0, 1],
                 [0, 0, 0, 0, 0, 1],
                 [0, 0, 0, 1, 1, 0]]

# Menu
print("MAIOR DISTÂNCIA ENTRE VÉRTICES EM UM GRAFO")
print("Escolha o grafo:")
print("1 - grafo_matriz1")
print("2 - grafo_matriz2")
print("3 - grafo_matriz3")
escolha = int(input("Digite sua escolha (1, 2 ou 3): "))

if escolha == 1:
    print("Maior distância do grafo 1:", maior_distancia(grafo_matriz1))
elif escolha == 2:
    print("Maior distância do grafo 2:", maior_distancia(grafo_matriz2))
elif escolha == 3:
    print("Maior distância do grafo 3:", maior_distancia(grafo_matriz3))
else:
    print("Opção inválida.")