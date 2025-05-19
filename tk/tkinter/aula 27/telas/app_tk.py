import tkinter as tk 
from tkinter import Entry, messagebox

from modelos.pedido import Pedido
from modelos.item_pedido import ItemPedido

from servico.salvar import salvar_pedido
class AppTk:
    def __init__(self,janela):
        janela.title('Cadastro de itens')

        janela.geometry("900x600+10+10")
        janela.config(bg='pink')
        


        tk.Label( text="Infome o Nome do cliente :,",font=("helvetica",16,"bold"),bg="#900",fg="white",).grid(row=0, column=0, sticky='w')
        tk.Label( text="Informe o item comprado :",font=("helvetica",16,"bold"),bg="#900",fg="white",).grid(row=1, column=0, sticky='w')
        tk.Label( text="Informe a quantidade comprada:",font=("helvetica",16,"bold"),bg="#900",fg="white").grid(row=2, column=0, sticky='w')
        tk.Label( text="Informe o proço do Produto:",font=("helvetica",16,"bold"),bg="#900",fg="white",).grid(row=3, column=0, sticky='w')


        self.ent_nome = Entry()
        self.ent_item= Entry()
        self.ent_qtd = Entry()
        self.ent_preco = Entry()
        
        



        self.ent_nome.grid(row=0, column=1)
        self.ent_item.grid(row=1, column=1)
        self.ent_qtd.grid(row=2, column=1)
        self.ent_preco.grid(row=3, column=1)

        tk.Button( text="Cadastrar", command=self.salvar_itens).grid(row=4, column=0, columnspan=2)

    def salvar_itens(self):
        nome = self.ent_nome.get()
        item = self.ent_item.get()
        qtd = self.ent_qtd.get()
        preco = self.ent_preco.get()
        
        if(not nome or not item or not qtd or not preco):
            messagebox.showwarning("Atenção", "Todos os itens devem ser preenchidos! ")
            return

        item_pedido = ItemPedido(item, int (qtd),float(preco))
        item_pedido2 =ItemPedido('maça',2, 20.50)
        pedido1 = Pedido(nome, '001', '20/05/2025', item_pedido, item_pedido2)

        salvar_pedido(pedido1.mostrar())
        messagebox.showinfo('cadastro', 'prooduto cadastrado com sucesso')