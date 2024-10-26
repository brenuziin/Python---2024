#'janela.resizable(False,False)' - Bloquea a maximização da janela.

import customtkinter as ctk

ctk.set_appearance_mode('system')
janela = ctk.CTk()
janela.geometry('500x500')


def imc():
    p = int(peso.get())
    a = float(altura.get())
    calculo = p/(a*a)
    
    if(calculo<18.5):
        situacao = 'Magro'
    if(calculo>=18.5 and calculo<25):
        situacao = 'Peso Ideal'
    if(calculo>=25 and calculo<30):
        situacao = 'Sobrepeso'
    else:
        situacao = 'Obesidade'
    
    resultado.configure(text=f'O seu IMC é {calculo:.2f} \n Sua Situação: {situacao}')
                        

ctk.CTkLabel(janela,
             text='Aplicativo de Saúde 2024 - Brenuzin',
             text_color= 'red',
             font=('Arial', 25, 'bold')).pack(pady=10)

peso = ctk.CTkEntry(janela,
                    width=400,
                    height=40,
                    placeholder_text='Digite a porra do seu peso')

peso.pack(pady=10)

altura= ctk.CTkEntry(janela,
                    width=400,
                    height=40,
                    placeholder_text='Digite a porra da sua altura')
altura.pack(pady=10)

botao = ctk.CTkButton(janela,
                      width=200,
                      height=30,
                      text='Clica nessa pora mermão',
                      font=('Arial',15),
                      command=imc)
botao.pack(pady=10)

resultado = ctk.CTkLabel(janela,
                         text='',
                         font=('Arial',20))
resultado.pack(pady=10)

janela.mainloop()