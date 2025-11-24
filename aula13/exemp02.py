import pandas as pd

dados = {
    'Nome': ['Alice','Bob','Carlos'],
    'Idade': [23,30,35],
    'Salario': [5000,6000,7000]
}
df = pd.DataFrame(dados)
df['Bonus'] = df ['Salario']*0.1
# Excluir coluna
df = df.drop(columns=['Bonus'])
print(df)

# print(df[df['Idade'] > 28])