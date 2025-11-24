idade = float(input("Digite sua idade: "))

if idade < 0:
    print("Como você tá digitando aqui se você nem sequer nasceu ainda?")
elif idade < 18:
    print("Você é um menor de idade")
elif idade < 65:
    print("Você é um adulto")
elif idade < 123:
    print("Você é um idoso")
else:
    print("Como que tu tá vivo ainda?")