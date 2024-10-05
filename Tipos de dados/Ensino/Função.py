import os
os.system ("cls||clear")
def nome():
    nome = input(f"Digite o nome: ")
    sobrenome = input(f"Digite seu sobrenome: ")
    return f"{nome} {sobrenome}"

nomeCompleto = nome ()

numeroum =int(input(f"Digite seu 1° número: "))
numerodois = int(input(f"Digite seu 2° número: "))

soma = numeroum + numerodois

print(f"Olá {nomeCompleto}, tudo bem? sua soma deu {soma}")