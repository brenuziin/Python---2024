import os
os.system("cls || clear")

print("==== Solitando dados para o usuário ====")
produto = input("Digite qual produto deseja: ")
quanti = int(input("Digite quantas unidades deseja: "))
 
preco = 1.00

if quanti <=5:
    desconto = 0.02
elif quanti <=10:
    desconto = 0.03
else:
    desconto = 0.05

total = quanti* preco
totalPagar = total - (total * desconto)

os.system("cls || clear")
print("===== Exibindo Dados =====")
print(f"Produto escolhido: {produto}")
print(f"Quantidade desejada: {quanti}")
print(f"Desconto recebido: {desconto}")
print(f"Valor da compra: {totalPagar}")