import tkinter as tk
from tkinter import messagebox

def abrir_cadastro():
    cadastro_window = tk.Toplevel()
    cadastro_window.title("Cadastro")

    tk.Label(cadastro_window, text="📝 Cadastro", font=("Arial", 14)).pack(pady=10)

    tk.Label(cadastro_window, text="Nome:").pack()
    nome_entry = tk.Entry(cadastro_window)
    nome_entry.pack(pady=5)

    tk.Label(cadastro_window, text="Email:").pack()
    email_entry = tk.Entry(cadastro_window)
    email_entry.pack(pady=5)

    tk.Label(cadastro_window, text="Senha:").pack()
    senha_entry = tk.Entry(cadastro_window, show="*")
    senha_entry.pack(pady=5)

    def cadastrar():
        nome = nome_entry.get()
        email = email_entry.get()
        senha = senha_entry.get()
        if nome and email and senha:
            messagebox.showinfo("Cadastro", f"Usuário {nome} cadastrado com sucesso!")
            cadastro_window.destroy()
        else:
            messagebox.showwarning("Erro", "Por favor, preencha todos os campos.")

    tk.Button(cadastro_window, text="Cadastrar", command=cadastrar).pack(pady=10)

def login():
    email = email_entry.get()
    senha = senha_entry.get()
    if email and senha:
        messagebox.showinfo("Login", f"Login realizado com sucesso!\nEmail: {email}")
    else:
        messagebox.showwarning("Erro", "Por favor, preencha todos os campos.")

root = tk.Tk()
root.title("Tela de Login")

tk.Label(root, text="🔑 Tela de Login", font=("Arial", 14)).pack(pady=10)

tk.Label(root, text="Email:").pack()
email_entry = tk.Entry(root)
email_entry.pack(pady=5)

tk.Label(root, text="Senha:").pack()
senha_entry = tk.Entry(root, show="*")
senha_entry.pack(pady=5)

tk.Button(root, text="Login", command=login).pack(pady=10)
tk.Button(root, text="Cadastrar", command=abrir_cadastro).pack(pady=5)

root.mainloop()
