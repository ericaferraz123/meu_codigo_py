
# #Peça 5 números ao usuário, guarde-os
# # # em uma lista e calcule a média.
# import tkinter as tk
 
# janela = tk.Tk ()
# janela.title ('lista ')
 
# def pede_numero ():
#     lista_numeros = []
#     for numeros in range (5):
#       numeroLido = input ('Digite um numero: ')    
#     lista_numeros.append(numeroLido)
#     lb_numero = tk.Label (text= lista_numeros [numeros])
#     lb_numero.pack()

# #9
# import tkinter as tk
# def exibir_notas():
#     notas = [7.5, 9.0, 6.8, 8.4, 5.3, 10.0]
    
#     for i in range(5):
#         tk.Label(text=f"Nota {i+1}: {nota}").pack()
    
#     maior_nota = max(notas)
#     menor_nota = min(notas)
    
#     tk.Label(text=f"  Maior Nota: {maior_nota}").pack()
#     tk.Label (text=f"Menor Nota: {menor_nota}").pack()


# janela = tk.Tk()
# janela.config(background = "#619191")
# janela.geometry("400x300")
# janela.maxsize(width=1200, height=900)
# janela.minsize(width=400, height=200)

# janela.title("Notas dos Estudantes")
# exibir_notas()
# janela.mainloop()
#Crie uma lista de 5 idades e diga quantas são maiores de 18.
# import tkinter as tk
# janela = tk.Tk()

# def lista():
#     nomes = ['Érica', 'Rayane', 'Ferraz', 'Sanguina']
#     for nome in nomes:
#         nome_0 = tk.Label(text=nome)
#         nome_0.pack()
#         print(nome)
        
# lista()
# janela.mainloop()
# import tkinter as tk
# janela = tk.Tk()
# def numero_7():
#     numero
# for i in range(5):
#     idade = int(input(f"Digite a sua idade:"))
#     idade.append(idade)
#     maior_de_18_anos = 0
# for idade in idades: 
#     if idade > 18:
#         maiores_de_18_anos += 1
        
#     print(f"Existem {maiores_de_18_anos} pessoas maiores de 18 anos.")    
    
    

# janela .title("Maior de 18 Anos")

# janela.geometry("300x200")
# janela.mainloop()


import tkinter as tk
janela = tk.Tk()
janela.geometry("900x600+10+10")

lista_palavras = []
maior_palavra = ''

def cadastra_palavra():
    nova_palavra = entry_palavra.get()
    lista_palavras.append(nova_palavra)
    if len(nova_palavra) > len(maior_palavra):
        maior_palavra = nova_palavra
    print(lista_palavras)
    
lb_instrucao = tk.Label(text= 'Informe um palavra : ').pack()
entry_palavra = tk.Entry()
entry_palavra.pack()
bt_enviar = tk.Button(text= 'Enviar', command=cadastra_palavra ).pack()
janela.mainloop()