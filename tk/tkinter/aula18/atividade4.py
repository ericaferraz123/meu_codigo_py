import tkinter as tk
tupla_frutas=("maça","banana","laranja","pera","cereja","maça")
janela= tk.Tk()
janela.title("tupla fruta")
janela.config(bg='light yellow')
janela.geometry("600x400")
 
def exibi_fruta():
    tupla=tupla_frutas.count("maça")
    label_frutas.config(text=f"tem {tupla} maças")
     
 
 
botao_frutas = tk.Button(janela, text="exiba frutas ",command=exibi_fruta)
botao_frutas.pack(side="top")
 
label_frutas=tk.Label(janela,text="", bg='light yellow')
label_frutas.pack(side="top",pady=30,anchor="s")
janela.mainloop()