def dividir(a, b):
    try:
        resultado = a/b
    except ZeroDivisionError:
        print("Não existe divisão por zero")
        resultado = None
    else:
        print("Divisão realizada com sucesso!")
    finally:
        print("Operação finalizada")    

        return resultado

print(dividir(10, 2))
print(dividir(10, 0))