n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero: "))
op = input("Digite a operacao (+, -, x, /): ")

if op == '+':
    print("Resultado:", n1 + n2)
elif op == '-':
    print("Resultado:", n1 - n2)
elif op == 'x':
    print("Resultado:", n1 * n2)
elif op == '/':
    if n2 != 0:
        print("Resultado:", n1 / n2)
    else:
        print("Erro: divisao por zero!")
else:
    print("Operação invalida!")