import os

os.system ("clear || clear")

salario_bruto = int(input(f"Digite seu sálario Bruto: "))

if salario_bruto > 3500:
    desconto = salario_bruto * 0.05
    acrescimo = salario_bruto * 0.03
    salario_liquido = salario_bruto - desconto + acrescimo
else:
    desconto = salario_bruto * 0.04
    acrescimo = salario_bruto * 0.05
    salario_liquido = salario_bruto - desconto + acrescimo
os.system ("clear || clear")

print(f"Seu Sálario liquido: {salario_liquido}")
    