def maior_lista():
    lista = input("Digite números separados por espaço: ")
    numeros = [float(x) for x in lista.split()]
    return max(numeros)

print("Maior da lista =", maior_lista())