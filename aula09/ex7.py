def verificar_primo():
    num = int(input("Digite um número: "))
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

print("É primo?", verificar_primo())