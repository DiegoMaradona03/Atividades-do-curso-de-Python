numeros = []

for i in range(5):
    numero = float(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

media = sum(numeros) / len(numeros)

print("Os números digitados foram:", numeros)
print("A média é:", media)