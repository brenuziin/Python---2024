import os
os.system("cls || clear")

# Vetor começa pelo numero 0
x=[15,21,65,85,45]

# Append insere o numero na ultima posição
x.append(333)
# Insert insere o numero na posição que você queira
x.insert(0,25)

print(x)
print(x[4])
print(f"{x[2]}--{x[0]}--{x[1]}")