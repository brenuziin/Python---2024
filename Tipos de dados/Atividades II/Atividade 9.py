import os
os.system("cls || clear")

altura = float(input("Digite a altura da pessoa (em metros): "))

peso_ideal = (72.7 * altura) - 58

os.system("cls || clear")
print("O peso ideal para a altura de", altura, "metros é:", peso_ideal, "kg")