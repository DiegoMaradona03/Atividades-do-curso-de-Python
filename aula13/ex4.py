import pandas as pd
import numpy as np

dados = {
    'Produto': ['Impressora', 'Tablet', 'SSD', 'Mouse'],
    'Avaliações': [[5, 4, 4, 3], [4, 5, 5, 5], [5, 5, 5, 4], [3, 4, 3, 4]]
}

df = pd.DataFrame(dados)

df['Média Avaliações'] = df['Avaliações'].apply(np.mean)

filtro_media_alta = df[df['Média Avaliações'] >= 4.5]

df_ordenado = filtro_media_alta.sort_values(by='Média Avaliações', ascending=False)


print("Tabela Completa com Médias:\n", df)
print("\nProdutos com Média de Avaliações:\n", df_ordenado)