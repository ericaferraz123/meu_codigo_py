import tkinter as tk
from tkinter import messagebox
from models.cliente_pf import ClientePF # type: ignore

class ClienteApp:
    def __init__(self, janela):
        self.janela = janela
        janela.title("Cadastro de Cliente")
        janela.geometry("900x500+10+10")
        janela.config(bg="pink")

        tk.Label( text="Nome:").grid(row=0, column=0)
        tk.Label( text="Email:").grid(row=1, column=0)
        tk.Label( text="CPF:").grid(row=2, column=0)

        tk.Entry().grid(row=0, column=1)
        tk.Entry().grid(row=1, column=1)
        tk.Entry().grid(row=2, column=1)

        tk.Button( text="Cadastrar").grid(row=4, column=0, command=self.salvar_cliente)


    def salvar_cliente(self):
        nome = self.entry_nome.get()
        email = self.entry_email.get()
        cpf = self.entry_cpf.get()
        
        if(not nome or not email or not cpf):
            messagebox.showwarning("Atenção", "Todos os campos devem estar preeenchidos")
            return
        
        
        cliente = ClientePF(nome, email, cpf)
        self.salvar_cliente(cliente)
