import tkinter as tk
janela = tk.Tk()
janela.title('Frutas')
janela.geometry('400x600')
janela.config(bg='pink')

frutas_set = {"maçã", "banana", "abacaxi", "goiaba", "amora"}


label_fruta = tk.Label(janela, text="", bg='pink', font=("Arial", 12))
label_fruta.grid(pady=10)

def ver():
    frutas_set.add("laranja")
    label_fruta.config(text=(frutas_set))  

botao_fruta = tk.Button(janela, text='Exiba as Frutas', command=ver)
botao_fruta.grid()

janela.mainloop()
 
