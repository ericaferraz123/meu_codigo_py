# Crie uma pilha vazia e permita ao usuário empilhar 
# 5 números digitados. Em seguida,
# exiba o conteúdo da pilha.
# import tkinter as tk
# janela = tk.Tk()
 
 
# pilha = []
# entradas = []
 
# def exibir():
#     resultado_label.config(text=pilha)
   
# def empilhar_numeros():
#     for entrada in entradas:
#         numero = int(entrada.get())
#         pilha.append(numero)
       
#     resultado_label.config(text=f"{pilha}")
 
# for i in range(5):
#     label = tk.Label(janela, text=f"Número {i+1}:")
#     label.pack(pady=5)
#     entrada_numero = tk.Entry(janela)
#     entrada_numero.pack(pady=5)
#     entradas.append(entrada_numero)
 
 
 
# janela.title("Empilhe 5 Números")
# janela.config(background="Purple")
# janela.geometry("400x400")
# calcular_button = tk.Button(janela, text="Números digitados", command=empilhar_numeros)
# calcular_button.pack(pady=10)
 
# resultado_label = tk.Label(janela, text="")
# resultado_label.pack(pady=10)
 
# janela.mainloop()

#atividade 2 
# import tkinter as tk
 
# janela = tk.Tk()
# pilha = []
 
# def empilhar():
#     valor = entrada.get()
#     if valor == "sair":
#         resultado_label.config(text=f"Pilha final: {pilha}")
#     else:
#         pilha.append(valor)
#         resultado_label.config(text=f"Pilha atual: {pilha}")
#     entrada.delete(0, tk.END)
 
# janela.title("Empilhar até 'sair'")
# janela.config(background="blue")
# janela.geometry("400x400")
 
# label = tk.Label(janela, text="Digite um valor (ou 'sair'):")
# label.pack(pady=5)
 
# entrada = tk.Entry(janela)
# entrada.pack(pady=5)
 
# botao_empilhar = tk.Button(janela, text="Empilhar", command=empilhar)
# botao_empilhar.pack(pady=10)
 
# resultado_label = tk.Label(janela, text="")
# resultado_label.pack(pady=10)
 
# janela.mainloop()
# #atividade3 
# #exercico 2
# """import tkinter as tk
 
# pilha = []
 
# def empilhar():
#     valor = entrada.get()
#     if valor.lower() == 'sair':
#         janela.destroy()
#     else:
#         pilha.append(valor)
#         entrada.delete(0, tk.END)
#         pilha_label.config(text="Pilha: " + ', '.join(reversed(pilha)))
 
# janela = tk.Tk()
# janela.title("Empilhar até 'sair'")
 
# entrada = tk.Entry(janela)
# entrada.pack()
 
# botao = tk.Button(janela, text="Empilhar", command=empilhar)
# botao.pack()
 
# pilha_label = tk.Label(janela, text="Pilha:")
# pilha_label.pack()
 
# janela.mainloop()"""
 
# #exercico 3
# """import tkinter as tk
 
# pilha = ['a', 'b', 'c']
 
# def desempilhar():
#     if not pilha:
#         tk.messagebox.showwarning("Aviso", "⚠️ Pilha está vazia!")
#     else:
#         valor = pilha.pop()
#         tk.messagebox.showinfo("Desempilhado", f"Valor desempilhado: {valor}")
#         pilha_label.config(text="Pilha: " + ', '.join(reversed(pilha)))
 
# janela = tk.Tk()
# janela.title("Desempilhar")
# tk.messagebox = tk.messagebox  # Habilita uso sem import direto
 
# botao = tk.Button(janela, text="Desempilhar", command=desempilhar)
# botao.pack()
 
# pilha_label = tk.Label(janela, text="Pilha: " + ', '.join(reversed(pilha)))
# pilha_label.pack()
 
# janela.mainloop()"""
# # 4. Menu com várias opções
 
# """import tkinter as tk
 
# pilha = []
# tk.messagebox = tk.messagebox
 
# def empilhar():
#     valor = entrada.get()
#     pilha.append(valor)
#     entrada.delete(0, tk.END)
#     atualizar()
 
# def desempilhar():
#     if pilha:
#         valor = pilha.pop()
#         tk.messagebox.showinfo("Desempilhado", f"Desempilhado: {valor}")
#     else:
#         tk.messagebox.showwarning("Aviso", "⚠️ Pilha vazia.")
#     atualizar()
 
# def ver_topo():
#     if pilha:
#         tk.messagebox.showinfo("Topo", f"Topo da pilha: {pilha[-1]}")
#     else:
#         tk.messagebox.showwarning("Aviso", "⚠️ Pilha vazia.")
 
# def atualizar():
#     pilha_label.config(text="Pilha: " + ', '.join(reversed(pilha)))
 
# janela = tk.Tk()
# janela.title("Menu Pilha")
 
# entrada = tk.Entry(janela)
# entrada.pack()
 
# tk.Button(janela, text="Empilhar", command=empilhar).pack()
# tk.Button(janela, text="Desempilhar", command=desempilhar).pack()
# tk.Button(janela, text="Ver Topo", command=ver_topo).pack()
 
# pilha_label = tk.Label(janela, text="Pilha:")
# pilha_label.pack()
 
# janela.mainloop()"""
# #5. Tamanho da pilha
# """import tkinter as tk
 
# pilha = []
 
# tk.messagebox = tk.messagebox
 
# def empilhar():
#     valor = entrada.get()
#     pilha.append(valor)
#     entrada.delete(0, tk.END)
 
# def tamanho_pilha():
#     tk.messagebox.showinfo("Tamanho", f"Tamanho da pilha: {len(pilha)}")
 
# janela = tk.Tk()
# janela.title("Tamanho da Pilha")
 
# entrada = tk.Entry(janela)
# entrada.pack()
 
# tk.Button(janela, text="Empilhar", command=empilhar).pack()
# tk.Button(janela, text="Ver Tamanho", command=tamanho_pilha).pack()
 
# janela.mainloop()"""
#6. Pilha de nomes + busca
 
# import tkinter as tk
 
# pilha_nomes = []
# tk.messagebox = tk.messagebox []
 
# def empilhar():
#     nome = entrada.get()
#     if nome.lower() == 'sair':
#         janela.destroy()
#     else:
#         pilha_nomes.append(nome)
#         entrada.delete(0, tk.END)
#         atualizar()
 
# def buscar():
#     nome = entrada_busca.get()
#     if nome in pilha_nomes:
#         tk.messagebox.showinfo("Busca", "Nome encontrado!")
#     else:
#         tk.messagebox.showinfo("Busca", "Nome não está na pilha.")
 
# def atualizar():
#     pilha_label.config(text="Pilha: " + ', '.join(reversed(pilha_nomes)))
 
# janela = tk.Tk()
# janela.title("Pilha de Nomes")
 
# entrada = tk.Entry(janela)
# entrada.pack()
# tk.Button(janela, text="Empilhar", command=empilhar).pack()
# entrada_busca = tk.Entry(janela)
# entrada_busca.pack()
# tk.Button(janela, text="Buscar", command=buscar).pack()
 
# pilha_label = tk.Label(janela, text="Pilha:")
# pilha_label.pack()
 
# janela.mainloop()

# # #7. Botão voltar navegador
 
import tkinter as tk
 
navegador = []
tk.messagebox = tk.messagebox
 
def navegar():
    url = entrada.get()
    navegador.append(url)
    entrada.delete(0, tk.END)
    atualizar()
 
def voltar():
    if navegador:
        navegador.pop()
        atual = navegador[-1] if navegador else "Sem páginas"
        tk.messagebox.showinfo("Voltar", f"Página atual: {atual}")
    else:
        tk.messagebox.showwarning("Aviso", "⚠️ Nenhuma página para voltar.")
    atualizar()
 
def atualizar():
    label.config(text="Histórico: " + ' > '.join(navegador))
 
janela = tk.Tk()
janela.title("Navegador")
 
entrada = tk.Entry(janela)
entrada.pack()
tk.Button(janela, text="Navegar", command=navegar).pack()
tk.Button(janela, text="Voltar", command=voltar).pack()
 
label = tk.Label(janela, text="Histórico:")
label.pack()
 
janela.mainloop()
# # 8. Inverter palavra com .pop()
# """import tkinter as tk
 
# def inverter():
#     palavra = entrada.get()
#     pilha = list(palavra)
#     invertida = ''
#     while pilha:
#         invertida += pilha.pop()
#     resultado.config(text="Invertida: " + invertida)
 
# janela = tk.Tk()
# janela.title("Inverter Palavra")
 
# entrada = tk.Entry(janela)
# entrada.pack()
# tk.Button(janela, text="Inverter", command=inverter).pack()
 
# resultado = tk.Label(janela, text="")
# resultado.pack()
 
# janela.mainloop()"""
# #9. Verificar parênteses
 
# """import tkinter as tk
 
# tk.messagebox = tk.messagebox
 
# def verificar():
#     expr = entrada.get()
#     pilha = []
#     pares = {')': '(', ']': '[', '}': '{'}
 
#     for char in expr:
#         if char in '([{':
#             pilha.append(char)
#         elif char in ')]}':
#             if not pilha or pilha.pop() != pares[char]:
#                 tk.messagebox.showerror("Erro", "Parênteses incorretos.")
#                 return
#     if not pilha:
#         tk.messagebox.showinfo("Ok", "Parênteses corretos!")
#     else:
#         tk.messagebox.showerror("Erro", "Parênteses incorretos.")
 
# janela = tk.Tk()
# janela.title("Verificador de Parênteses")
 
# entrada = tk.Entry(janela)
# entrada.pack()
# tk.Button(janela, text="Verificar", command=verificar).pack()
 
# janela.mainloop()"""
# # 10. Calculadora RPN
# """import tkinter as tk
 
# tk.messagebox = tk.messagebox
 
# def calcular():
#     expr = entrada.get()
#     tokens = expr.split()
#     pilha = []
 
#     try:
#         for token in tokens:
#             if token.isdigit():
#                 pilha.append(int(token))
#             else:
#                 b = pilha.pop()
#                 a = pilha.pop()
#                 if token == '+': pilha.append(a + b)
#                 elif token == '-': pilha.append(a - b)
#                 elif token == '*': pilha.append(a * b)
#                 elif token == '/': pilha.append(a / b)
#         resultado.config(text="Resultado: " + str(pilha[0]))
#     except:
#         tk.messagebox.showerror("Erro", "Expressão inválida.")
 
# janela = tk.Tk()
# janela.title("Calculadora RPN")
 
# entrada = tk.Entry(janela)
# entrada.pack()
# tk.Button(janela, text="Calcular", command=calcular).pack()
 
# resultado = tk.Label(janela, text="")
# resultado.pack()
 
# janela.mainloop()
