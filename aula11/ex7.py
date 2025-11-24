def media_lista():
    try:
        entrada = input("Digite números separados por vírgula: ")
        numeros = [float(x.strip()) for x in entrada.split(",")]

        if len(numeros) == 0:
            raise ZeroDivisionError

        media = sum(numeros) / len(numeros)
        print(f"Média = {media}")

    except ValueError:
        print("Erro: digite apenas números separados por vírgula.")
    except ZeroDivisionError:
        print("Erro: não é possível calcular média de lista vazia.")

media_lista()