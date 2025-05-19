import tkinter as tk

def exibir_resultado(texto):
    resultado_text.delete("1.0", tk.END)
    resultado_text.insert(tk.END, texto)

def exercicio3():
    cores1 = {"vermelho", "azul", "verde"}
    cores2 = {"verde", "amarelo", "azul"}
    
    uniao = cores1.union(cores2)
    intersecao = cores1.intersection(cores2)
    diferenca = cores1.difference(cores2)
    
    resultado = (
        f"Cores 1: {cores1}\n"
        f"Cores 2: {cores2}\n\n"
        f"União: {uniao}\n"
        f"Interseção: {intersecao}\n"
        f"Diferença (1 - 2): {diferenca}"
    )
    
    exibir_resultado(resultado)

janela = tk.Tk()
janela.title("Conjuntos de Cores")
janela.geometry("500x400")
janela.config(bg="pink")
botao = tk.Button(janela, text="Mostre as cores", command=exercicio3)
botao.pack(pady=10)

resultado_text = tk.Text(janela, height=15, width=60)
resultado_text.pack(pady=10)

janela.mainloop()
