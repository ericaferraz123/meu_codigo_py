from tkinter import *
from tkinter import simpledialog

janela_principal = Tk()
janela_principal.geometry('400x300+10+10')
janela_principal.title("Fila de Atendimento")

def criar_interface_fila():
    fila_nomes = []
    senha_atual = [1]  # Usamos uma lista para passar por referência

    label_fila_texto = StringVar()
    label_fila_texto.set("Senhas na Fila:")
    label_fila_titulo = Label(textvariable=label_fila_texto, font=('Arial', 12, 'bold'), anchor='w')
    label_fila_titulo.pack(padx=20, anchor='w')

    lista_senhas_widget = Listbox( font=('Arial', 12))
    lista_senhas_widget.pack(pady=10, padx=20, fill=BOTH, expand=True)

    def gerar_nova_senha():
        nome = simpledialog.askstring('Novo Atendimento', 'Digite seu nome:')
        if nome:
            senha = f"A{senha_atual[0]:03d}"
            fila_nomes.append((senha, nome))
            atualizar_lista_senhas()
            senha_atual[0] += 1

    def atualizar_lista_senhas():
        lista_senhas_widget.delete(0, END)
        for senha, nome in fila_nomes:
            lista_senhas_widget.insert(END, f"{senha} - {nome}")

    btn_retirar_senha = Button(text='RETIRAR SENHA', command=gerar_nova_senha, bg='black', fg='white', font=('Helvetica', 12, 'bold'))
    btn_retirar_senha.pack(pady=20, ipadx=5, ipady=15)



criar_interface_fila()
janela_principal.mainloop()



# from tkinter import *
# from tkinter import simpledialog

# janela = Tk()
# janela.geometry('400x300+10+10')
# janela.title("Fila de Atendimento")

# fila_nomes = []
# senha_atual = 1
# lista_senhas = None

# def gerar_senha():
#     global senha_atual, lista_senhas, fila_nomes
#     nome = simpledialog.askstring('Novo Atendimento', 'Digite seu nome:')
#     if nome:
#         senha = f"A{senha_atual:03d}"
#         fila_nomes.append((senha, nome))
#         atualizar_lista_senhas()
#         senha_atual += 1

# def atualizar_lista_senhas():
#     global lista_senhas, fila_nomes
#     if lista_senhas:
#         lista_senhas.delete(0, END)
#         for senha, nome in fila_nomes:
#             lista_senhas.insert(END, f"{senha} - {nome}")
#     else:
#         lista_senhas = Listbox(janela, font=('Arial', 12))
#         lista_senhas.pack(pady=10, padx=20, fill=BOTH, expand=True)
#         for senha, nome in fila_nomes:
#             lista_senhas.insert(END, f"{senha} - {nome}")

# btn_retirar_senha = Button(janela, text='RETIRAR SENHA', command=gerar_senha, font=('Helvetica', 14, 'bold'))
# btn_retirar_senha.pack(pady=20)

# label_fila = Label(janela, text="Senhas na Fila:", font=('Arial', 12, 'bold'), anchor='w')
# label_fila.pack(padx=20, anchor='w')

# atualizar_lista_senhas()

# janela.mainloop()