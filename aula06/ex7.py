a = float(input("Digite o primeiro lado do triangulo: "))
b = float(input("Digite o segundo lado do triangulo: "))
c = float(input("Digite o terceiro lado do triangulo: "))

if a + b <= c or a + c <= b or b + c <= a:
    print("Os lados nao formam um triangulo valido.")
elif a == b == c:
    print("Triangulo equilatero.")
elif a == b or a == c or b == c:
    print("Triangulo isosceles.")
else:
    print("Triangulo escaleno.")