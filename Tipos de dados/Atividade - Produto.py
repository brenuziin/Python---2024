import os

os.system("clear")

notaUm = float(input("Digite seu 1° valor: "))
notaDois = float(input("Digite seu 2° valor: "))

soma = notaUm + notaDois
produto = notaUm * notaDois
media = soma /2
maior = max(notaUm, notaDois)
menor = min(notaUm, notaDois)


if notaUm > notaDois:
    print(f"Maior número: {notaUm}")
    print(f"Menor número: {notaDois}")

elif notaDois > notaUm:
    print(f"Maior número: {notaDois}")
    print(f"Menor número: {notaUm}")

print(f"Soma dos números: {soma}")
print(f"Média Aritmetrica: {media}")
print(f"Seu produto: {produto}")