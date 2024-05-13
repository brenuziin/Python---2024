notas = []

while True:
    print("Menu:")
    print("S - Inserir mais uma nota")
    print("P - Ver quantas notas foram inseridas")
    print("N - Calcular a média aritmética das notas")
    opcao = input("Escolha uma opção: ")

    if opcao == 'S':
        nota = float(input("Digite a nota: "))
        notas.append(nota)
    elif opcao == 'P':
        print(f"Foram inseridas {len(notas)} notas.")
    elif opcao == 'N':
        if len(notas) == 0:
            print("Nenhuma nota foi inserida ainda.")
        else:
            media = sum(notas) / len(notas)
            print(f"A média aritmética: {media}")
    else:
        print("Opção inválida.")

    true_opcao = input("Deseja continuar (S/N)? ").upper()
    if continuar_opcao != 'S':
        continuar = False
