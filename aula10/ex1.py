def dividir():
        try:
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            resultado = a/b
        except ZeroDivisionError:
            print("Não existe divisão por zero")
            resultado = None
        except ValueError:
            print("digite apenas números")
            resultado = None
        else:
            print("Divisão realizada com sucesso!")
        finally:
            print("Operação finalizada")    

        return resultado

print(dividir())