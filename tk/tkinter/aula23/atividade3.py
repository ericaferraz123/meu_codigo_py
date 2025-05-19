#criar um sistema simples de gerenciaento de estoque,
# com as seguintes funcionalidades:
# Adicionar produto ao dicionario (nome:Quantidade)
#Atualizar qauntidade de estoque 
#Remover produto
#Exibir todos os produtos Disponiveis com for.
import tkinter as tk

estoque = {}
def adicionar_produto():
    nome = entrada_nome.get()
    quantidade = entrada_quantidade.get()

    try:
        if nome not in estoque:
            estoque [nome] = float(quantidade)
            label_estoque.config(text=f"Produto {nome} adicionado")
        else:
            label_estoque.config(text=f"Produto de {nome} já existe.")
    except ValueError:
        label_estoque.config(text="Erro digite uma quantidade válida")

def atualizar_produto():
    nome = entrada_nome.get()
    quantidade = entrada_quantidade.get()
    try:
        if nome in estoque:
            estoque[nome] = float(quantidade)
            label_estoque.config(text=f"Quantidade de '{nome}' atualizada")
        else:
            label_estoque.config(text="Produto não encontrado")
    except ValueError:
        label_estoque.config(text="Erro: Digite uma quantidade válida")

 
def remover_produto():
    nome = entrada_nome.get()
    if nome in estoque:
        del estoque[nome]
        label_estoque.config(text=f"Produto '{nome}' removido.")
    else:
        label_estoque.config(text="Produto não encontrado.")
 
 
def exibir_produto():
    if estoque:
        texto = "Produtos disponíveis:\n"
        for nome, qtd in estoque.items():
            texto += f"{nome}: {qtd}\n"
    else:
        texto = "Estoque vazio."
    label_estoque.config(text=texto)












janela = tk.Tk()
janela.title("Quantidade de Estoque")
janela.config(bg="#ffe6f0") 
janela.geometry("400x400")

tk.Label(janela, text="Nome do Produto:", bg="#ffb6c1").grid(row=0, column=0, padx=5, pady=5)
entrada_nome = tk.Entry(janela)
entrada_nome.grid(row=0, column=1, padx=5, pady=5)

tk.Label(janela, text="Quantidade:", bg="#ffb6c1").grid(row=1, column=0, padx=5, pady=5)
entrada_quantidade = tk.Entry(janela)
entrada_quantidade.grid(row=1, column=1, padx=5, pady=5)



tk.Button(janela, text="Adicionar", command=adicionar_produto, bg="#ffb6c1").grid(row=2, column=0, pady=10)
tk.Button(janela, text="Atualizar", command=atualizar_produto, bg="#ffb6c1").grid(row=2, column=1)
tk.Button(janela, text="Remover", command=remover_produto, bg="#ffb6c1").grid(row=2, column=2, padx=5)
tk.Button(janela, text="Exibir", command=exibir_produto, bg="#ffb6c1").grid(row=2, column=3, padx=5)

label_estoque = tk.Label(janela, text="", bg="#ffe6f0")
label_estoque.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

janela.mainloop()
