
from tkinter import *
from tkinter import simpledialog, messagebox

janela = Tk()
janela.geometry('400x300+10+10')
janela.title("Cadastro de Nomes")

fila = []
lb_fila = None

def atualizar_fila():
    global lb_fila
    fila_texto = "\n".join(fila)
    if lb_fila:
        lb_fila.config(text=fila_texto)
    else:
        lb_fila = Label(janela, text=fila_texto, font=('Arial', 12), justify='left')
        lb_fila.pack(pady=10, padx=20, anchor='w')

def adicionar_nome():
    nome = simpledialog.askstring("Adicionar Nome", "Digite um nome (ou 'sair' para finalizar):")
    if nome is not None:
        if nome.lower() == 'sair':
            messagebox.showinfo("Fila Finalizada", "Cadastro de nomes finalizado.")
        elif nome.strip():
            fila.append(nome.strip())
            atualizar_fila()
        else:
            messagebox.showerror("Erro", "Por favor, digite um nome válido.")

btn_adicionar = Button(janela, text='Adicionar Nome', command=adicionar_nome, font=('Helvetica', 12))
btn_adicionar.pack(pady=20)

lb_titulo_fila = Label(janela, text="Fila de Nomes:", font=('Arial', 14, 'bold'), anchor='w')
lb_titulo_fila.pack(padx=20, anchor='w')

atualizar_fila()

janela.mainloop()