numeros = list(range(1, 11))
for n in numeros[:]:
    if n % 2 == 0:
        numeros.remove(n)

print("Números ímpares:", numeros)
