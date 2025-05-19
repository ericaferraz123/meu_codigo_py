import tkinter as tk
from telas.app import App

def main():
    janela= tk.Tk()
    janela.title("Cadastro Pedido")
    janela.geometry("900x600+10+10")
    janela.config(bg='pink')
    def mostrar_tela_pedido():
        App(janela)
 
    botao_pedido = tk.Button(janela, text="Cadastro Pedido", command=mostrar_tela_pedido)
    botao_pedido.grid(rowspan=10, column=2)
 
    janela.mainloop()
 
if __name__ == "__main__":
    main()