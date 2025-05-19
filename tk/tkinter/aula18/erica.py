import tkinter as tk
from tkinter import font

# Criação da janela principal
janela = tk.Tk()
janela.title("Coleção de Números")
janela.geometry("350x300")
janela.config(bg="#FADADD")  # tom suave de rosa

numeros = set()

# Função para adicionar número
def numeros_():
    entrada = numeros_digitados.get()
    if entrada.strip():  # Adiciona somente se não for vazio
        numeros.add(entrada.strip())
        numeros_digitados.delete(0, tk.END)

# Função para exibir números
def exibir_():
    resultado.config(text=", ".join(sorted(numeros)))

# Estilo das fontes
fonte_titulo = font.Font(family="Helvetica", size=14, weight="bold")
fonte_padrao = font.Font(family="Arial", size=11)

# Título
titulo = tk.Label(janela, text="Digite e armazene números", bg="#FADADD", fg="#333", font=fonte_titulo)
titulo.pack(pady=(10, 5))

# Campo de entrada
frame_entrada = tk.Frame(janela, bg="#FADADD")
frame_entrada.pack(pady=10)

label_numero = tk.Label(frame_entrada, text="Número:", bg="#FADADD", font=fonte_padrao)
label_numero.pack(side="left", padx=(0, 10))

numeros_digitados = tk.Entry(frame_entrada, font=fonte_padrao, width=20)
numeros_digitados.pack(side="left")

# Botões
frame_botoes = tk.Frame(janela, bg="#FADADD")
frame_botoes.pack(pady=10)

botao_adicionar = tk.Button(frame_botoes, text="Adicionar", command=numeros_, bg="#FFB6C1", font=fonte_padrao)
botao_adicionar.pack(side="left", padx=10)

botao_exibir = tk.Button(frame_botoes, text="Exibir números", command=exibir_, bg="#FFB6C1", font=fonte_padrao)
botao_exibir.pack(side="left", padx=10)

# Resultado
resultado = tk.Label(janela, text="", bg="#FADADD", wraplength=300, font=fonte_padrao, fg="#444")
resultado.pack(pady=20)

# Inicia o loop da interface
janela.mainloop()
