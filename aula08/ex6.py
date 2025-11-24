paises = ["Brasil", "Argentina", "Japão", "Canadá", "Itália"]

print("Lista de países disponíveis:", paises)

verificar = input("Digite o nome de um país: ")

if verificar.lower() in [p.lower() for p in paises]:
    print(f"{verificar} está na lista!")
else:
    print(f"{verificar} não está na lista.")