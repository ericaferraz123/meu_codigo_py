import tkinter as tk
janela = tk.Tk()

    
tupla_frutas = ('maça', 'banana', 'ameixa', ' goiaba', 'amora')
def ver ():

    for fruta in tupla_frutas: 
        tk.Label(text=fruta). pack()

adicionar_button = tk.Button(janela, text= 'Exiba as Frutas', command=ver)
adicionar_button.pack(pady=5)
label_fruta = tk.Label(text="  ")
janela.title('Frutas')
janela.geometry('400x600')
janela.config( bg='pink')
janela.mainloop()
