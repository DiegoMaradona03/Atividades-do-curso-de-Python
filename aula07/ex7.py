n = int(input("Digite um número para ver a tabuada: "))

print(f"Tabuada do {n}:")
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")