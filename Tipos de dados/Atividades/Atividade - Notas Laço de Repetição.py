import os
os.system("cls || clear")

contador = 0

print("==== Solitando dados para o usuário ====")
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

for i in range(1,4):
    nota = float(input(f"Digite sua {i}° Nota: "))
    contador += nota

media = contador / 3
os.system("cls || clear")
print("==== Exibindo dados do usuário ====")
print(f"Nome do Aluno: {nome}")
print(f"Idade do Aluno: {idade} anos")
print(f"Soma das Unidades: {contador}")
print(f"Média Aritmetrica: {media}")

if media > 7:
    print("O aluno foi Aprovado!!!")

elif media < 6.9 and media > 6:
    print("O aluno está em Recuperação!!!") 

elif media < 5:
    print("O aluno foi Reprovado!!!")