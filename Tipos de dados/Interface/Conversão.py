#intalar o ctk - pip install customtkinter
import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode('dark')

def calculo():
    v = float (valor.get())
    c = float (cotacao.get())
    
    valorfinal = v*c
    messagebox.showinfo("Resultado", f"O valor convertido é R${valorfinal}")

janela = ctk.CTk()
janela.geometry("400x250")
janela.resizable(False, False)

janela.title("Sistema de converção")
janela.iconbitmap("logo_orange_nike_icon_134358.ico")

ctk.CTkLabel(janela, text="Sistema de Conveção",
             text_color="Red",
             font=("arial",20,"bold")).pack(pady=20)

valor = ctk.CTkEntry(janela,
                     width=275,
                     height=35,
                     placeholder_text="Digite seu valor")
valor.pack()

cotacao = ctk.CTkEntry(janela,
                       width=275,
                       height=35,
                       placeholder_text="Digite o valor do Dollar atualmente!")
cotacao.pack(pady=10)

button = ctk.CTkButton(janela,
                       text="Aperte aqui",
                       text_color="red",
                       fg_color="black",
                       command=calculo)
button.pack(pady=10)

janela.mainloop()
