from tkinter import Tk, Button, simpledialog, messagebox,Toplevel


janela = Tk()
janela.title("Exemplos com Dicionários")
def janela_contato ():
    contato = {}
    def adicionar_contato():
        nome = simpledialog.askstring("Contato", "Nome")
        telefone = simpledialog.askinteger("Nome", " Telefone: ")
        if nome and telefone:
            contato[nome] =  telefone
            messagebox.showinfo("Sucesso", f"{contato}")
    janela = Toplevel()
    janela.title("Dicionario de contatos")
    Button(janela, text="adicionar contato", command=adicionar_contato).pack()

def janela_agenda():
    agenda = {}

    def adicionar_compromisso():
        data = simpledialog.askstring("Agenda", "Data (dd-mm-aaaa):")
        evento = simpledialog.askstring("Agenda", "Descrição do evento:")
        if data and evento:
            agenda[data] = evento
            messagebox.showinfo("Sucesso", f"Compromisso adicionado: {data}: {evento}")
    janela = Toplevel()
    janela.title("Agenda de Compromissos")
    Button(janela, text="Adicionar compromisso", command=adicionar_compromisso).pack(pady=5)

def janela_preco():
    produtos = {}
    def calcular_media():
        produto = simpledialog.askinteger("Produto", "Adicione quantos produtos:")
        calcular = simpledialog.askinteger("Média", " Digite o Preço:")
        if produto and calcular:
            produtos[produto] = calcular 
        media = sum(produtos) / (calcular)
        print(f'A média do preço é: {media}')
    janela = Toplevel()
    janela.title("Dicionário de Preços")
    Button(janela, text="Calcular média", command=calcular_media).pack(pady=5)

def janela_remover():
    produtos = {}
    def remover_produtos():
        produto = simpledialog.askstring("Produto", "Adicione o produto:")
        preco = simpledialog.askinteger("Preço", "Digite o preço:")

        if produto and preco is not None:
            produtos[produto] = preco
            produtos_filtrados = {
                nome: valor for nome,
                valor in produtos.items() 
                if valor >= 10
            }
            mensagem = "   ".join([f"{nome}: R${valor}" for nome, valor in produtos_filtrados.items()])
            if not mensagem:
                mensagem = "Nenhum produto com preço acima de R$10."
            messagebox.showinfo("Produtos Removidos", mensagem)
    janela = Toplevel()
    janela.title("Dicionario de Produtos removidos")
    Button(janela, text="produtos", command=remover_produtos).pack(pady=5)
    
def janela_verificar():
    def verificar_precos():
        verificar = { }
        preco = simpledialog.askstring("Preço", "Adicione preço do produto :")

        if preco in verificar:

            messagebox.showinfo("Resultado", f"{preco} está no dicionário.")
        else:

            messagebox.showinfo("Resultado", f"{preco} não está no dicionário.")
    janela = Toplevel()
    janela.title("Dicionario de Produtos removidos")
    Button(janela, text="produtos", command=verificar_precos).pack(pady=5)
        
funcoes = [
    ("1. Contatos", janela_contato),
    ("2. Agenda", janela_agenda),
    ("3. Preços Médio", janela_preco),
    ("4. Remover preços", janela_remover),
    ("5. Verificar Produto", janela_verificar),
    # ("6. Alunos", janela_mostrar_alunos),
    # ("7. Atualizar Veículo", janela_atualizar_veiculo),
    # ("8. Somar Estoque", janela_somar_estoque),
    # ("9. Total da Compra", janela_calcular_compra),
    # ("10. Boletim Escolar", janela_mostrar_boletim)


]
for texto, func in funcoes:
    Button(janela, text=texto, width = 30, command=func).pack(padx=10,pady= 5)

janela.mainloop()
