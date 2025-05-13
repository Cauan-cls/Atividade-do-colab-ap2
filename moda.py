#Moda:

#Tempo: O(n²) no pior caso (lista sem repetições).

#Espaço: O(n) (listas auxiliares de contagem).



def moda(lista):
    elementos = []
    contagens = []

    for i in range(len(lista)):
        item = lista[i]
        encontrado = False
        for j in range(len(elementos)):
            if elementos[j] == item:
                contagens[j] += 1
                encontrado = True
                break
        if not encontrado:
            elementos.append(item)
            contagens.append(1)

    maior = 0
    indice_maior = 0
    for i in range(len(contagens)):
        if contagens[i] > maior:
            maior = contagens[i]
            indice_maior = i

    return elementos[indice_maior]

# Listas de teste
lista1 = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9]
lista2 = [i//10 for i in range(100, -10, -1)] + [10,11,12,13,14,5,16,17,18,19]
lista3 = [(i**3)//1000 for i in range(100, -10, -1)]

# Menu
print("MODA ESTATÍSTICA")
print("Escolha a lista para calcular a moda:")
print("1 - lista1 = [0, 1, 0, 2, ..., 9]")
print("2 - lista2 = [i//10 for i in range(100, -10, -1)] + [..., 19]")
print("3 - lista3 = [(i**3)//1000 for i in range(100, -10, -1)]")
escolha = int(input("Digite sua escolha (1, 2 ou 3): "))

if escolha == 1:
    print("Moda da lista1:", moda(lista1))
elif escolha == 2:
    print("Moda da lista2:", moda(lista2))
elif escolha == 3:
    print("Moda da lista3:", moda(lista3))
else:
    print("Opção inválida.")