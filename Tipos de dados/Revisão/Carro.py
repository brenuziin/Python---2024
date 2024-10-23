import os
os.system("cls || clear")

carro = int(input(f"Qual velocidade seu carro estava?: "))
os.system("cls || clear")
print(f"Seu carro estava com a velocidade de {carro} km/h")

if carro >= 80:
    limite = carro - 80
    multa = limite * 5
    print(f"Você ultrapassou o limite de velocidade. E recebeu uma multa no valor de R$ {multa:.2f}")
else:
    print("Você esta dentro dos limites de velocidade.")