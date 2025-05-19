# import tkinter as tk
# from tkinter import messagebox

# class Cliente:
#     def __init__(self, nome, telefone):
#         self.nome = nome
#         self.telefone = telefone

# class Pedido:
#     def __init__(self, numero, valor_total, cliente):
#         self.numero = numero
#         self.valor_total = valor_total
#         self.cliente = cliente

#     def salvar(self):
#         try:
#             with open("pedidos.txt", "a") as arquivo:
#                 linha = f"Pedido {self.numero:03d} | R$ {self.valor_total:.2f} | Cliente: {self.cliente.nome} - Tel: {self.cliente.telefone}\n"
#                 arquivo.write(linha)
#             return True, f"Pedido {self.numero:03d} salvo com sucesso!"
#         except IOError:
#             return False, "Erro ao gravar o pedido no arquivo."

# class CadastroPedido:
#     def __init__(self, master):
#         self.master = master
#         master.title("Cadastro de Pedido")

#         self.label_nome = tk.Label(master, text="Nome do Cliente:")
#         self.label_nome.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
#         self.entry_nome = tk.Entry(master)
#         self.entry_nome.grid(row=0, column=1, padx=5, pady=5)

#         self.label_telefone = tk.Label(master, text="Telefone do Cliente:")
#         self.label_telefone.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
#         self.entry_telefone = tk.Entry(master)
#         self.entry_telefone.grid(row=1, column=1, padx=5, pady=5)

#         self.label_numero_pedido = tk.Label(master, text="Número do Pedido:")
#         self.label_numero_pedido.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
#         self.entry_numero_pedido = tk.Entry(master)
#         self.entry_numero_pedido.grid(row=2, column=1, padx=5, pady=5)

#         self.label_valor_total = tk.Label(master, text="Valor Total do Pedido:")
#         self.label_valor_total.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
#         self.entry_valor_total = tk.Entry(master)
#         self.entry_valor_total.grid(row=3, column=1, padx=5, pady=5)

#         self.botao_cadastrar = tk.Button(master, text="Cadastrar Pedido", command=self.cadastrar_pedido)
#         self.botao_cadastrar.grid(row=4, column=0, columnspan=2, pady=10)

#     def cadastrar_pedido(self):
#         nome_cliente = self.entry_nome.get()
#         telefone_cliente = self.entry_telefone.get()
#         numero_pedido = self.entry_numero_pedido.get()
#         valor_total_pedido = self.entry_valor_total.get()

#         if not all([nome_cliente, telefone_cliente, numero_pedido, valor_total_pedido]):
#             messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
#             return

#         try:
#             numero_pedido = int(numero_pedido)
#             valor_total_pedido = float(valor_total_pedido)
#         except ValueError:
#             messagebox.showerror("Erro", "Número do pedido e valor total devem ser numéricos.")
#             return

#         cliente = Cliente(nome_cliente, telefone_cliente)
#         pedido = Pedido(numero_pedido, valor_total_pedido, cliente)
#         sucesso, mensagem = pedido.salvar()

#         if sucesso:
#             messagebox.showinfo("Sucesso", mensagem)
#             self.limpar_campos()
#         else:
#             messagebox.showerror("Erro", mensagem)

#     def limpar_campos(self):
#         self.entry_nome.delete(0, tk.END)
#         self.entry_telefone.delete(0, tk.END)
#         self.entry_numero_pedido.delete(0, tk.END)
#         self.entry_valor_total.delete(0, tk.END)

# if __name__ == "__main__":
#     janela = tk.Tk()
#     app = CadastroPedido(janela)
#     janela.mainloop()
import tkinter as tk
from tkinter import messagebox

# Classes
class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

    def __str__(self):
        return f'Nome: {self.nome}, Telefone: {self.telefone}'

class Pedido:
    def __init__(self, numero, valor_total, cliente):
        self.numero = numero
        self.valor_total = valor_total
        self.cliente = cliente

    def salvar(self, arquivo='pedidos.txt'):
        try:
            with open(arquivo, 'a', encoding='utf-8') as f:
                f.write(f'Pedido Nº: {self.numero}\n')
                f.write(f'Valor Total: R$ {self.valor_total:.2f}\n')
                f.write(f'{self.cliente}\n')
                f.write('---\n')
            return True
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar o pedido: {e}")
            return False

# Função para processar os dados da interface
def salvar_pedido():
    try:
        numero = int(entry_numero.get())
        valor = float(entry_valor.get())
        nome = entry_nome.get()
        telefone = entry_telefone.get()

        if not nome or not telefone:
            raise ValueError("Nome e telefone não podem estar vazios.")

        cliente = Cliente(nome, telefone)
        pedido = Pedido(numero, valor, cliente)

        if pedido.salvar():
            messagebox.showinfo("Sucesso", "Pedido salvo com sucesso!")
            # Limpar campos
            entry_numero.delete(0, tk.END)
            entry_valor.delete(0, tk.END)
            entry_nome.delete(0, tk.END)
            entry_telefone.delete(0, tk.END)
    except ValueError as ve:
        messagebox.showerror("Erro de entrada", str(ve))

# Interface gráfica
root = tk.Tk()
root.title("Cadastro de Pedido")

tk.Label(root, text="Número do Pedido:").grid(row=0, column=0, sticky="e")
entry_numero = tk.Entry(root)
entry_numero.grid(row=0, column=1)

tk.Label(root, text="Valor Total:").grid(row=1, column=0, sticky="e")
entry_valor = tk.Entry(root)
entry_valor.grid(row=1, column=1)

tk.Label(root, text="Nome do Cliente:").grid(row=2, column=0, sticky="e")
entry_nome = tk.Entry(root)
entry_nome.grid(row=2, column=1)

tk.Label(root, text="Telefone do Cliente:").grid(row=3, column=0, sticky="e")
entry_telefone = tk.Entry(root)
entry_telefone.grid(row=3, column=1)

btn_salvar = tk.Button(root, text="Salvar Pedido", command=salvar_pedido)
btn_salvar.grid(row=4, columnspan=2, pady=10)

root.mainloop()
