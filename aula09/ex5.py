def maior_numero():
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    return a if a > b else b

print("Maior número =", maior_numero())