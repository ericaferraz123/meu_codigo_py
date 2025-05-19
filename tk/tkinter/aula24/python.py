# from tkinter import Tk, Button, simpledialog, messagebox
 
# janela = Tk()

# janela.title("Exemplos com Dicionários")

# janela.geometry("400x500")
 
# # 1. Contatos

# def mostrar_contatos():

#     contatos = {"Ana": "99999-1111", "Carlos": "98888-2222", "João": "97777-3333"}

#     msg = "\n".join([f"{nome}: {telefone}" for nome, telefone in contatos.items()])

#     messagebox.showinfo("Contatos", msg)
 
# # 2. Agenda

# def mostrar_agenda():

#     agenda = {"2025-05-10": "Reunião com equipe", "2025-05-15": "Consulta médica"}

#     msg = "\n".join([f"{data}: {evento}" for data, evento in agenda.items()])

#     messagebox.showinfo("Agenda", msg)
 
# # 3. Média de preços

# def media_precos():

#     produtos = {"Arroz": 25.0, "Feijão": 8.5, "Carne": 45.0}

#     media = sum(produtos.values()) / len(produtos)

#     messagebox.showinfo("Média de Preços", f"Média: R${media:.2f}")
 
# # 4. Remover produtos abaixo de R$10

# def remover_produtos_baratos():

#     produtos = {"Arroz": 25.0, "Feijão": 8.5, "Carne": 45.0}

#     produtos_filtrados = {k: v for k, v in produtos.items() if v >= 10}

#     msg = "\n".join([f"{k}: R${v}" for k, v in produtos_filtrados.items()])

#     messagebox.showinfo("Produtos >= R$10", msg)
 
# # 5. Verificar chave

# def verificar_chave():

#     produtos = {"Arroz": 25.0, "Feijão": 8.5}

#     chave = simpledialog.askstring("Verificação", "Qual produto deseja verificar?")

#     if chave in produtos:

#         messagebox.showinfo("Resultado", f"{chave} está no dicionário.")

#     else:

#         messagebox.showinfo("Resultado", f"{chave} não está no dicionário.")
 
# # 6. Cadastro de alunos

# def mostrar_alunos():

#     alunos = {

#         "Maria": {"nota": 7.5, "status": "Aprovada"},

#         "Lucas": {"nota": 4.0, "status": "Reprovado"}

#     }

#     msg = "\n".join([f"{nome}: Nota {dados['nota']} - {dados['status']}" for nome, dados in alunos.items()])

#     messagebox.showinfo("Alunos", msg)
 
# # 7. Atualizar veículo

# def atualizar_veiculo():

#     veiculo = {"marca": "Toyota", "modelo": "Corolla", "ano": 2020}

#     novo_ano = simpledialog.askinteger("Atualizar Veículo", "Novo ano do veículo:")

#     if novo_ano:

#         veiculo["ano"] = novo_ano

#         messagebox.showinfo("Veículo Atualizado", f"{veiculo}")
 
# # 8. Somar estoque

# def somar_estoque():

#     estoque = {"camisa": 10, "calça": 5, "tênis": 8}

#     total = sum(estoque.values())

#     messagebox.showinfo("Estoque", f"Total: {total} itens")
 
# # 9. Total da compra

# def calcular_compra():

#     cardapio = {"Pizza": 30, "Refrigerante": 7, "Hambúrguer": 15}

#     pedido = simpledialog.askstring("Pedido", "Itens separados por vírgula (ex: Pizza,Refrigerante):")

#     if pedido:

#         itens = [item.strip() for item in pedido.split(",")]

#         total = sum([cardapio.get(item, 0) for item in itens])

#         messagebox.showinfo("Total da Compra", f"Total: R${total}")
 
# # 10. Boletim escolar

# def mostrar_boletim():

#     boletim = {"Matemática": 6.5, "Português": 8.0, "História": 4.0}

#     msg = ""

#     for disc, nota in boletim.items():

#         status = "Aprovado" if nota >= 6 else "Reprovado"

#         msg += f"{disc}: {nota} - {status}\n"

#     messagebox.showinfo("Boletim", msg)
 
# # Botões

# botoes = [

#     ("Contatos", mostrar_contatos),

#     ("Agenda", mostrar_agenda),

#     ("Média de Preços", media_precos),

#     ("Remover Produtos Baratos", remover_produtos_baratos),

#     ("Verificar Produto", verificar_chave),

#     ("Alunos", mostrar_alunos),

#     ("Atualizar Veículo", atualizar_veiculo),

#     ("Somar Estoque", somar_estoque),

#     ("Total da Compra", calcular_compra),

#     ("Boletim Escolar", mostrar_boletim)

# ]
 
# for i, (texto, funcao) in enumerate(botoes):

#     Button(janela, text=texto, command=funcao, width=30).grid(row=i, column=0, pady=5, padx=10)
 
# janela.mainloop()

class Cliente:
    def __init__(self, nome, CPF, email, telefone):
        self.nome = nome
        self.CPF = CPF
        self.email = email
        self.telefone = telefone

    def __str__(self):
        return f"Cliente: {self.nome} -- CPF: {self.CPF} -- Email: {self.email} -- Telefone: {self.telefone}"


# Subclasse com herança e polimorfismo
class ClienteVIP(Cliente):
    def __init__(self, nome, CPF, email, telefone, nivel_vip):
        super().__init__(nome, CPF, email, telefone)
        self.nivel_vip = nivel_vip  # atributo novo

    # Polimorfismo: sobrescrevendo o método __str__
    def __str__(self):
        return (f"Cliente VIP: {self.nome} -- CPF: {self.CPF} -- Email: {self.email} "
                f"-- Telefone: {self.telefone} -- Nível VIP: {self.nivel_vip}")


# Exemplos de uso
cliente1 = Cliente("Érica Ferraz", "109.763.876.27", "erica@email.com", "99999-9999")
cliente2 = ClienteVIP("Carlos Silva", "111.222.333-44", "carlos@email.com", "98888-8888", "Ouro")

# Impressão polimórfica
print(cliente1)  # Usa o método __str__ da classe Cliente
print(cliente2)  # Usa o método __str__ da classe ClienteVIP
