import random

numeros = [random.randint(1, 100) for _ in range(10)]
print("Números:", numeros)
print("Maior número:", max(numeros))
print("Menor número:", min(numeros))