import os 
import random
os.system("cls || clear")

saladeaula = []
while True :
    aluno = input(f"Digite o nome do aluno:")
    if(aluno=="saida"):
        break 
    else: saladeaula.append(aluno)
os.system("cls || clear")
sorteado = random.choice(saladeaula)

print(f"O aluno sorteado foi: {sorteado}")