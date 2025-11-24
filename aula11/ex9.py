class DivisorZeroError(Exception):
    pass

def dividir_custom(a, b):
    if b == 0:
        raise DivisorZeroError("Divisão por zero não permitida.")
    return a / b

try:
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    print(dividir_custom(a, b))
except DivisorZeroError as erro:
    print("Erro:", erro)
except ValueError:
    print("Digite valores numéricos válidos.")