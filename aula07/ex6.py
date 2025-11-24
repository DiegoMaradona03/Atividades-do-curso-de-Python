import random

numero_secreto = random.randint(1, 10)
tentativa = 0
contador = 0

print("=== Jogo de Adivinhacao ===")
print("Tente adivinhar o número entre 1 e 10!")

while tentativa != numero_secreto:
    tentativa = int(input("Digite seu palpite: "))
    contador += 1

    if tentativa > numero_secreto:
        print("Muito alto! Tente um número menor.")
    elif tentativa < numero_secreto:
        print("Muito baixo! Tente um número maior.")
    else:
        print(f"Parabens! Você acertou em {contador} tentativas!")