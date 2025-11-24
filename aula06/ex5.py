n1 = float(input("Digite sua nota de 0 a 100: "))

if n1 < -101 or n1 > 100:
    print("Nota invalida!")
elif n1 >= 50:
    print("Aprovado!")
elif n1 >= 0:
    print("Reprovado!")
else:
    print("Sua nota foi tão baixa mas tão baixa que só vou te dizer uma coisa... volta pro fundamental que tá precisando")