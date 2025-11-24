def fatorial():
    n = int(input("Digite um número: "))
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

print("Fatorial =", fatorial())