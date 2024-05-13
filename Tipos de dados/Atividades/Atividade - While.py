import os

os.system("clear")

nota = float (input("Digite o 1° número: "))
notaD = float (input("Digite o 2° número: "))

while (nota < 0 or nota > 10):
    nota = float(input("Digite um número entre 0 a 10: "))

while (notaD < 0 or notaD > 10):
    notaD = float(input("Digite um número entre 0 a 10: "))

soma = nota + notaD
media = soma / 2

print(f"Soma das notas informadas: {soma}")
print(f"Media Aritmetrica: {media}")