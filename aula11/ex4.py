import math

def raiz_quadrada():
    try:
        n = float(input("Digite um número para calcular a raiz quadrada: "))
        if n < 0:
            raise ValueError("Não existe raiz quadrada real de número negativo.")
        resultado = math.sqrt(n)
        print(f"Raiz quadrada = {resultado}")
    except ValueError as erro:
        print("Erro:", erro)

raiz_quadrada()