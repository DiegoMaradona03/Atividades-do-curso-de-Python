frutas = ["maçã", "banana", "laranja", "uva", "manga"]

print("Lista inicial de frutas:", frutas)

for i in range(3):
    nova_fruta = input(f"Digite o nome da {i+1}ª fruta adicional: ")
    frutas.append(nova_fruta)

print("Lista final de frutas:", frutas)