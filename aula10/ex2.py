def ler_inteiro():
    try:
        n = int(input("Digite um número inteiro: "))
        print(f"Você digitou o número {n}")
    except ValueError:
        print("Erro: digite apenas números inteiros.")

ler_inteiro()