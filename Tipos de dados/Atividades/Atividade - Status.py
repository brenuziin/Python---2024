import os
os.system("cls || clear")

print("Solitando dados para o usuário")
nome = input("Digite seu nome: ")
sexo = input("Digite seu sexo: ")
estado = input("Digite seu estado civil: ")

sexo = sexo.lower()
estado = estado.lower()

if sexo == "feminino" and estado == "casada":
    tempo = input("Quantos anos de casado?: ")

os.system("cls || clear")
print("==== Exibindo dados do usuário ====")
print(f"Nome: {nome}")
print(f"Sexo: {sexo}")
print(f"Estado Civil: {estado}")
if sexo == "feminino" and estado == "casada":
    print(f"Casada há: {tempo} anos")