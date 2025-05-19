import tkinter as tk
janela = tk.Tk()

tupla_frutas = ('maça', 'banana', 'ameixa', ' goiaba', 'amora')
def ver ():
    print(tupla_frutas[3])
    label_fruta.config(text=tupla_frutas[3])

adicionar_button = tk.Button(janela, text= 'Exiba as Frutas', command=ver)
adicionar_button.pack(pady=5)
label_fruta = tk.Label(text="   " , bg='pink')
label_fruta.pack(pady=5)
janela.title('Frutas')
janela.geometry('400x600')
janela.config( bg='pink')
janela.mainloop()
