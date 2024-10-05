import tkinter as tk

def calcular():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operacao = operacao_var.get()

        if operacao == "Soma":
            resultado = num1 + num2
        elif operacao == "Subtração":
            resultado = num1 - num2
        elif operacao == "Multiplicação":
            resultado = num1 * num2
        elif operacao == "Divisão":
            if num2 != 0:
                resultado = num1 / num2
            else:
                resultado_label.config(text="Erro: Divisão por zero!")
                return

        resultado_label.config(text=f"Resultado: {resultado}")
    except ValueError:
        resultado_label.config(text="Erro: Insira números válidos!")

root = tk.Tk()
root.title("Calculadora Simples")

label_num1 = tk.Label(root, text="Número 1:")
label_num1.pack(pady=5)

entry_num1 = tk.Entry(root)
entry_num1.pack(pady=5)

label_num2 = tk.Label(root, text="Número 2:")
label_num2.pack(pady=5)

entry_num2 = tk.Entry(root)
entry_num2.pack(pady=5)

operacao_var = tk.StringVar(value="Soma")

label_operacao = tk.Label(root, text="Escolha a operação:")
label_operacao.pack(pady=5)

operacoes = ["Soma", "Subtração", "Multiplicação", "Divisão"]
for operacao in operacoes:
    radio_button = tk.Radiobutton(root, text=operacao, variable=operacao_var, value=operacao)
    radio_button.pack(anchor='w')

button_calcular = tk.Button(root, text="Calcular", command=calcular)
button_calcular.pack(pady=20)

resultado_label = tk.Label(root, text="")
resultado_label.pack(pady=20)

root.mainloop()
