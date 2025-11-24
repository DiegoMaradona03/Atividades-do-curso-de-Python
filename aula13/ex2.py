import pandas as pd

dados = {
    'Item': ['Pendrive', 'Headset', 'WebCam', 'Teclado MK'],
    'Quantidade':[25,12,8,15],
    'Preço Unitário':[30, 150, 220, 95]
}
df = pd.DataFrame(dados)

df ['Total'] = df['Preço Unitário'] * df['Quantidade']

media_precos = df['Preço Unitário'].mean()

filtro = df[df['Preço Unitário'] > 100]

print("Tabela Completa:\n",df)
print(f"\nMédia Geral de preços unitários R$: {media_precos:.2f}")
print("\nProdutos acima de R$100: \n", filtro)