import tkinter as tk
tupla_frutas=("maça","abacaxi","laranja","pera","cereja")
janela= tk.Tk()
janela.title("tupla fruta")
janela.config(bg='purple')
janela.geometry("600x400")
 
def exibi_fruta():
    if "abacaxi" in tupla_frutas:
        label_frutas.config(text="tem abacaxi na tupla")
    else:
        label_frutas.config(text="nao tem abacaxi na tupla")
     
 
 
botao_frutas = tk.Button(janela, text="exiba frutas ",command=exibi_fruta)
botao_frutas.pack(side="top")
 
label_frutas=tk.Label(janela,text="", bg='purple')
label_frutas.pack(side="right")
janela.mainloop()