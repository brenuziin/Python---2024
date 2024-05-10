import os

os.system("clear")

login = input("Digite seu login: ")
senha = input("Insira sua senha: ")

if login == "Brenuzin" and senha == "1545":
    print("Olá Patrão seja bem vindo novamente!")
else:
    print("Não foi possivel acessar digite novamente, seu login e senha!")

