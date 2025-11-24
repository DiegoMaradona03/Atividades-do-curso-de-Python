import pandas as pd

dados = {
    'Produto': ['Caderno', 'Lápis', 'Mochila', 'Borracha'],
    'Preço':[12,2,85,80],
    'Vendidos':[40, 150, 10, 80]
}
df = pd.DataFrame(dados)

df ['Faturamento'] = df['Preço'] * df['Vendidos']

df = df.sort_values(by='Produto', ascending=True)

filtro = df[df['Faturamento'] > 500]

print("Tabela Completa:\n",df)
print("\nProdutos com faturamento acima de R$500: \n", filtro)