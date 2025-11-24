def acessar_lista():
    lista = [10, 20, 30]
    try:
        indice = int(input("Digite um índice para acessar (0 a 2): "))
        print(f"Valor encontrado: {lista[indice]}")
    except ValueError:
        print("Erro: digite um número inteiro para o índice.")
    except IndexError:
        print("Erro: índice fora do alcance da lista.")

acessar_lista()