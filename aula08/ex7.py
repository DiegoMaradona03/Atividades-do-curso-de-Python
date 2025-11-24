notas = []

for i in range(10):
    nota = float(input(f"Digite a nota do {i+1}º aluno: "))
    notas.append(nota)

media = sum(notas) / len(notas)
maior = max(notas)
menor = min(notas)

print("\nNotas digitadas:", notas)
print("Média da turma:", media)
print("Maior nota:", maior)
print("Menor nota:", menor)