import os
os.system("cls || clear")

print("Solicitando salário do funcionário")
salario = float(input("Digite seu salário: "))

os.system("cls || clear")
valor = salario * 1.35

print(f"Valor do seu Salário: R${salario}")
print(f"Salário reajustado em 35%: R${round(valor, 2)}")