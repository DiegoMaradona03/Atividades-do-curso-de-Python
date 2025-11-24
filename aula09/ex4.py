def par_ou_impar():
    numero = int(input("Digite um número: "))
    return "Par" if numero % 2 == 0 else "Ímpar"

print("O número é:", par_ou_impar())