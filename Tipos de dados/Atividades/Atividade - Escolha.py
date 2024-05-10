import os
os.system("cls || clear")
a = int(input("Digite seu 1° Número: "))
b = int(input("Digite seu 2° Número: "))
opcao = input("Digite a opção desejada: ")

match(opcao):
    case "+":
        resultado = a + b
    case "-":
        resultado = a - b
    case "*":
        resultado = a * b
    case "/":
        resultado = a / b
    case _:
        print("Opção Inválida")        

print(f"Resultado do calculo: {resultado}")