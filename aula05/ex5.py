valorHora = float(input("Quanto voce ganha por hora? "))
horas = float(input("Quantas horas você trabalhou durante o mês? "))

salarioBruto = valorHora * horas
ir = salarioBruto * 0.11
inss = salarioBruto * 0.08
sindicato = salarioBruto * 0.05

salarioLiquido = salarioBruto - ir - inss - sindicato

print(f"+ Salario Bruto : R$ {salarioBruto:.2f}")
print(f"- IR (11%)      : R$ {ir:.2f}")
print(f"- INSS (8%)     : R$ {inss:.2f}")
print(f"- Sindicato (5%): R$ {sindicato:.2f}")
print(f"= Salario Liquido: R$ {salarioLiquido:.2f}")