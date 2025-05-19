import tkinter as tk
janela = tk.Tk()
numeros = set()
def numeros_():
    entrada = numeros_digitados.get()
    numeros.add(entrada)

def exibir_():
    resultado.config(text=numeros)

janela.title("numero")
janela.geometry("300x200")
janela.config(bg="pink")


numero = tk.Label(text="Digite um número:")
numero.grid(pady=10)

numeros_digitados = tk.Entry()
numeros_digitados.grid(pady=10)


botao_exibir = tk.Button(janela, text= "Exibir números", command= exibir_)
botao_exibir.grid()
botao = tk.Button(janela, text="Adicionar", command=numeros_)
botao.grid(pady=20)

resultado = tk.Label(janela, text="")
resultado.grid(pady=20)

janela.mainloop()