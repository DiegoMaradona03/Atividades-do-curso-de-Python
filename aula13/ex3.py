import pandas as pd

dados = {
    'Nome': ['Ana Souza', 'João Lima', 'Carla Mendes', 'Pedro Rocha'],
    'idade':[28,32,41,22],
    'Salário':[3500, 4200, 5100, 2800]
}
df = pd.DataFrame(dados)

df = df.sort_values(by='Salário', ascending=False)

media_salario = df['Salário'].mean()

filtro_acima_media = df[df['Salário'] > media_salario]

filtro = df[df['idade'] < 30]

print("Tabela Completa:\n",df)
print(f"\nMédia Salarial Geral: R$ {media_salario:.2f}")
print("\nFuncionários com Salário acima da média:\n", filtro_acima_media)
print("\nFuncionários com menos de 30 anos: \n", filtro)