import os
os.system("cls || clear")

print("==== Solitando dados para o usuário ====")
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
notaUm = float(input("Digite sua primeira Nota: "))
notaDois = float(input("Digite sua segunda Nota: "))
notaTres = float(input("Digite sua terceira Nota: "))

soma = notaUm + notaDois + notaTres
media = soma / 3

print("==== Exibindo dados do usuário ====")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Primeira Nota: {notaUm}")
print(f"Segunda Nota: {notaDois}")
print(f"Soma das Unidades: {soma}")
print(f"Média Aritmetrica: {round(media,2)}")

if media > 7:
    print("O aluno foi Aprovado!!!")

elif media < 6.9 and media > 6:
    print("O aluno está em Recuperação!!!") 

elif media < 5:
    print("O aluno foi Reprovado!!!")