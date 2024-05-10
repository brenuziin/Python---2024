import os
os.system("cls || clear")
pares = 0
impares = 0

for i in range(1,6):
    numero = int(input(f"Digite seu {i}° Número: "))

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Quantidade de Pares: {pares}")
print(f"Quantidade de Ímpares: {impares}")