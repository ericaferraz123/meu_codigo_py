#atividade1
# import tkinter as tk
#
# def mostrar_nomes():
#     nomes = ["João", "Maria", "Carlos", "Ana", "Lucas"]
#     for nome in nomes:
#         resultado_label.config(text=f"{nome}")

# janela = tk.Tk()
# janela.title("Exibir Nomes")
# janela.geometry("300x200")

# titulo_label = tk.Label(janela, text="Exibindo Nomes", font=("Helvetica", 14))
# titulo_label.pack(pady=10)

# mostrar_botao = tk.Button(janela, text="Mostrar Nomes", command=mostrar_nomes)
# mostrar_botao.pack(pady=10)

# resultado_label = tk.Label(janela, text="", font=("Helvetica", 12))
# resultado_label.pack(pady=10)

# janela.mainloop()


#atividade 2
# import tkinter as tk

# def calcular_media():
#     numeros = [int(entrada1.get()), int(entrada2.get()), int(entrada3.get()), int(entrada4.get()), int(entrada5.get())]
#     media = sum(numeros) / len(numeros)
#     resultado_label.config(text=f"Média: {media:.2f}")

# janela = tk.Tk()
# janela.title("Calcular Média")
# janela.geometry("300x200")

# titulo_label = tk.Label(janela, text="Digite 5 números", font=("Helvetica", 14))
# titulo_label.pack(pady=10)

# entrada1 = tk.Entry(janela)
# entrada1.pack()
# entrada2 = tk.Entry(janela)
# entrada2.pack()
# entrada3 = tk.Entry(janela)
# entrada3.pack()
# entrada4 = tk.Entry(janela)
# entrada4.pack()
# entrada5 = tk.Entry(janela)
# entrada5.pack()

# calcular_button = tk.Button(janela, text="Calcular Média", command=calcular_media)
# calcular_button.pack(pady=10)

# resultado_label = tk.Label(janela, text="", font=("Helvetica", 12))
# resultado_label.pack(pady=10)

# janela.mainloop()


# atividade 3 

# import tkinter as tk

# def maior_palavra():
#     palavras = [entrada1.get(), entrada2.get(), entrada3.get(), entrada4.get(), entrada5.get()]
#     maior = max(palavras, key=len)
#     resultado_label.config(text=f"A maior palavra é: {maior}")

# janela = tk.Tk()
# janela.title("Maior Palavra")
# janela.geometry("300x200")

# titulo_label = tk.Label(janela, text="Digite 5 palavras", font=("Helvetica", 14))
# titulo_label.pack(pady=10)

# entrada1 = tk.Entry(janela)
# entrada1.pack()
# entrada2 = tk.Entry(janela)
# entrada2.pack()
# entrada3 = tk.Entry(janela)
# entrada3.pack()
# entrada4 = tk.Entry(janela)
# entrada4.pack()
# entrada5 = tk.Entry(janela)
# entrada5.pack()

# calcular_button = tk.Button(janela, text="Ver Maior Palavra", command=maior_palavra)
# calcular_button.pack(pady=10)

# resultado_label = tk.Label(janela, text="", font=("Helvetica", 12))
# resultado_label.pack(pady=10)

# janela.mainloop()

#atividade 4 

# import tkinter as tk

# def mostrar_pares():
#     numeros = [int(entrada1.get()), int(entrada2.get()), int(entrada3.get()), int(entrada4.get()), int(entrada5.get()), int(entrada6.get()), int(entrada7.get()), int(entrada8.get()), int(entrada9.get()), int(entrada10.get())]
#     pares = [str(num) for num in numeros if num % 2 == 0]
#     resultado_label.config(text="Números pares: " + ", ".join(pares))

# janela = tk.Tk()
# janela.title("Mostrar Pares")
# janela.geometry("300x350")

# titulo_label = tk.Label(janela, text="Digite 10 números", font=("Helvetica", 14))
# titulo_label.pack(pady=10)

# entrada1 = tk.Entry(janela)
# entrada1.pack()
# entrada2 = tk.Entry(janela)
# entrada2.pack()
# entrada3 = tk.Entry(janela)
# entrada3.pack()
# entrada4 = tk.Entry(janela)
# entrada4.pack()
# entrada5 = tk.Entry(janela)
# entrada5.pack()
# entrada6 = tk.Entry(janela)
# entrada6.pack()
# entrada7 = tk.Entry(janela)
# entrada7.pack()
# entrada8 = tk.Entry(janela)
# entrada8.pack()
# entrada9 = tk.Entry(janela)
# entrada9.pack()
# entrada10 = tk.Entry(janela)
# entrada10.pack()

# calcular_button = tk.Button(janela, text="Mostrar Pares", command=mostrar_pares)
# calcular_button.pack(pady=10)

# resultado_label = tk.Label(janela, text="", font=("Helvetica", 12))
# resultado_label.pack(pady=10)

# janela.mainloop()

#  atividade 5 

import tkinter as tk

produtos = []

def adicionar_produto():
    produto = entrada_produto.get()
    produtos.append(produto)
    lista_produtos_label.config(text=f"Produtos: {', '.join(produtos)}")

def remover_produto():
    produto = entrada_produto.get()
    if produto in produtos:
        produtos.remove(produto)
        lista_produtos_label.config(text=f"Produtos: {', '.join(produtos)}")
    else:
        lista_produtos_label.config(text="Produto não encontrado.")

janela = tk.Tk()
janela.title("Produtos")
janela.geometry("300x250")

titulo_label = tk.Label(janela, text="Adicione e remova produtos", font=("Helvetica", 14))
titulo_label.pack(pady=10)

entrada_produto = tk.Entry(janela)
entrada_produto.pack()

adicionar_button = tk.Button(janela, text="Adicionar Produto", command=adicionar_produto)
adicionar_button.pack(pady=5)

remover_button = tk.Button(janela, text="Remover Produto", command=remover_produto)
remover_button.pack(pady=5)

lista_produtos_label = tk.Label(janela, text="Produtos: ", font=("Helvetica", 12))
lista_produtos_label.pack(pady=10)

janela.mainloop()

#atividade 6

# import tkinter as tk

# def contar_maiores_18():
#     idades = [int(entrada1.get()), int(entrada2.get()), int(entrada3.get()), int(entrada4.get()), int(entrada5.get())]
#     maiores_18 = sum(1 for idade in idades if idade > 18)
#     resultado_label.config(text=f"Maiores de 18: {maiores_18}")

# janela = tk.Tk()
# janela.title("Contar Maiores de 18")
# janela.geometry("300x250")

# titulo_label = tk.Label(janela, text="Digite 5 idades", font=("Helvetica", 14))
# titulo_label.pack(pady=10)

# entrada1 = tk.Entry(janela)
# entrada1.pack()
# entrada2 = tk.Entry(janela)
# entrada2.pack()
# entrada3 = tk.Entry(janela)
# entrada3.pack()
# entrada4 = tk.Entry(janela)
# entrada4.pack()
# entrada5 = tk.Entry(janela)
# entrada5.pack()

# calcular_button = tk.Button(janela, text="Contar Maiores de 18", command=contar_maiores_18)
# calcular_button.pack(pady=10)

# resultado_label = tk.Label(janela, text="", font=("Helvetica", 12))
# resultado_label.pack(pady=10)

# janela.mainloop()

#atividade 7

# import tkinter as tk

# def verificar_nome():
#     nomes = [entrada1.get(), entrada2.get(), entrada3.get(), entrada4.get(), entrada5.get(), entrada6.get(), entrada7.get()]
#     if nome_especifico.get() in nomes:
#         resultado_label.config(text=f"{nome_especifico.get()} está na lista.")
#     else:
#         resultado_label.config(text=f"{nome_especifico.get()} não está na lista.")

# janela = tk.Tk()
# janela.title("Verificar Nome")
# janela.geometry("300x350")

# titulo_label = tk.Label(janela, text="Digite 7 nomes", font=("Helvetica", 14))
# titulo_label.pack(pady=10)

# entrada1 = tk.Entry(janela)
# entrada1.pack()
# entrada2 = tk.Entry(janela)
# entrada2.pack()
# entrada3 = tk.Entry(janela)
# entrada3.pack()
# entrada4 = tk.Entry(janela)
# entrada4.pack()
# entrada5 = tk.Entry(janela)
# entrada5.pack()
# entrada6 = tk.Entry(janela)
# entrada6.pack()
# entrada7 = tk.Entry(janela)
# entrada7.pack()

# nome_especifico = tk.Entry(janela)
# nome_especifico.pack()

# verificar_button = tk.Button(janela, text="Verificar Nome", command=verificar_nome)
# verificar_button.pack(pady=10)

# resultado_label = tk.Label(janela, text="", font=("Helvetica", 12))
# resultado_label.pack(pady=10)

# janela.mainloop()

#atividade 8 

# import tkinter as tk

# def ordenar_lista():
#     numeros = [int(entrada1.get()), int(entrada2.get()), int(entrada3.get()), int(entrada4.get()), int(entrada5.get())]
#     numeros.sort()
#     resultado_label.config(text=f"Lista ordenada: {', '.join(map(str, numeros))}")

# janela = tk.Tk()
# janela.title("Ordenar Lista")
# janela.geometry("300x250")

# titulo_label = tk.Label(janela, text="Digite 5 números", font=("Helvetica", 14))
# titulo_label.pack(pady=10)

# entrada1 = tk.Entry(janela)
# entrada1.pack()
# entrada2 = tk.Entry(janela)
# entrada2.pack()
# entrada3 = tk.Entry(janela)
# entrada3.pack()
# entrada4 = tk.Entry(janela)
# entrada4.pack()
# entrada5 = tk.Entry(janela)
# entrada5.pack()

# ordenar_button = tk.Button(janela, text="Ordenar Lista", command=ordenar_lista)
# ordenar_button.pack(pady=10)

# resultado_label = tk.Label(janela, text="", font=("Helvetica", 12))
# resultado_label.pack(pady=10)

# janela.mainloop()

#atividade9

# import tkinter as tk
# #Aqui estamos importando a biblioteca
# # Tkinter para criar a interface gráfica
# # . O tk é um apelido que usamos para
# # facilitar o uso da biblioteca.

# def mostrar_maior_menor():
#     notas = []
    
#     for entrada in [linha1, linha2, linha3, linha4, linha5, linha6]:
#         valor = entrada.get()
#         if not valor.replace('.', '', 1).isdigit():
#             label_resultado.config(text="Por favor, insira apenas números válidos.")
# #Função mostrar_maior_menor: Essa função é chamada quando o botão é pressionado.
# # Ela vai buscar os valores das 6 caixas de entrada (onde o usuário digita as notas),
# # verificando se são números válidos.
            
            
#             return  
#         notas.append(float(valor))
    
#     maior = max(notas)
#     menor = min(notas)

# #Verificação do número: A função valor.replace('.', '', 1).isdigit()
# # verifica se o valor inserido é um número válido. Ela permite que o número 
# # tenha um ponto (para números decimais), mas não aceita letras
# # ou caracteres inválidos.


#     label_resultado.config(text=f"Maior Nota: {maior}, Menor Nota: {menor}")

# janela = tk.Tk()
# janela.title("Maior e Menor Nota")
# #Define o título da janela (aparece na parte de cima da janela).
# janela.config(background="#f5aecf")
# janela.geometry("400x400")
# #Define o tamanho inicial da janela para 400 pixels de largura e 400 pixels de altura.
# janela.maxsize(width=1200, height=900)
# janela.minsize(width=400, height=300)


# label_instrucao = tk.Label(janela, text="Digite 6 notas:", fg="#ffffff", bg="#5f3999", font=("Slab", 12))
# label_instrucao.pack()

# linha1 = tk.Entry(janela)
# linha1.pack(pady=5)
# linha2 = tk.Entry(janela)
# linha2.pack(pady=5)
# linha3 = tk.Entry(janela)
# linha3.pack(pady=5)
# linha4 = tk.Entry(janela)
# linha4.pack(pady=5)
# linha5 = tk.Entry(janela)
# linha5.pack(pady=5)
# linha6 = tk.Entry(janela)
# linha6.pack(pady=5)
# #Aqui, são criadas 6 caixas de entrada (Entry)
# # para o usuário digitar as 6 notas. A função pack() 
# # coloca as caixas de entrada na janela e o pady=5 adiciona
# # um pouco de espaço vertical entre elas.

# novo_botao = tk.Button(janela, text="Mostrar Maior e Menor Nota", bg='#5f3999', fg='#d6cee0', command=mostrar_maior_menor)
# novo_botao.pack(pady=10)
# label_resultado = tk.Label(janela, text="Resultado", font=("Slab", 12), background="#c2a7bf")
# label_resultado.pack()
# janela.mainloop()
#(): Inicia o loop principal da janela.
# Isso significa que a janela vai ficar aberta e
# aguardando as interações do usuário (como clicar
# no botão ou digitar nas caixas de entrada).


#atividade 10 

# import tkinter as tk

# alunos = []

# def cadastrar_aluno():
#     nome = entrada_nome.get()
#     if nome.lower() != "sair":
#         alunos.append(nome)
#         lista_alunos_label.config(text=f"Alunos cadastrados: {', '.join(alunos)}")
#     else:
#         lista_alunos_label.config(text=f"Cadastro encerrado. Alunos: {', '.join(alunos)}")
#         entrada_nome.config(state="disabled")

# janela = tk.Tk()
# janela.title("Cadastro de Alunos")
# janela.geometry("500x250")

# titulo_label = tk.Label(janela, text="Digite o nome do aluno (Digite 'sair' para encerrar)", font=("Helvetica", 14))
# titulo_label.pack()

# entrada_nome = tk.Entry(janela)
# entrada_nome.pack()

# cadastrar_button = tk.Button(janela, text="Cadastrar Aluno", command=cadastrar_aluno)
# cadastrar_button.pack()

# lista_alunos_label = tk.Label(janela, text="Alunos cadastrados: ", font=("Helvetica", 12))
# lista_alunos_label.pack()

# janela.mainloop()
