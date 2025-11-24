def acessar_dicionario():
    pessoa = {
        "nome": "Diego",
        "idade": 18,
        "curso": "Desenvolvimento de Sistemas"
    }

    try:
        chave = input("Digite a chave que deseja acessar: ")
        print(f"Valor: {pessoa[chave]}")
    except KeyError:
        print("Erro: chave não encontrada no dicionário.")

acessar_dicionario()