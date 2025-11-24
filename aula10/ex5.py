def ler_arquivo():
    nome = "dados.txt"
    try:
        with open(nome, "r") as arquivo:
            conteudo = arquivo.read()
            print("Conteúdo do arquivo:")
            print(conteudo)
    except FileNotFoundError:
        print("Arquivo não encontrado. Criando arquivo...")
        with open(nome, "w") as arquivo:
            arquivo.write("O arquivo não existia. Criado automaticamente.\n")

ler_arquivo()