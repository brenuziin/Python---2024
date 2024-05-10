import os
os.system("cls || clear")

numero = int(input("Digite um número para tabuada: "))
os.system("cls || clear")
for i in range(1,11):
    print(f"{numero} x {i} = {numero * i}")