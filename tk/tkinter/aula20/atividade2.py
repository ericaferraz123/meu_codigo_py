import tkinter as tk 
janela = tk.Tk()

frutas_set = {}

frutas_set = set(frutas_set)

def adicionar():
    
    entrada = entrada_usuario.get()
    frutas_set.add(entrada)
    label_conjunto.config(text=frutas_set)

    
def remover_frutas():
    entrada = entry_remover.get()
    frutas_set.discard(entrada)
    label_conjunto.config(text=frutas_set)

label_adicionar = tk.Label(text="Digite a Fruta Desejada")
entrada_usuario = tk.Entry()
entrada_usuario.grid()



tk_button = tk.Button(text="adicionar",command= adicionar)
tk_button.grid()

label_remover = tk.Label(text="Digite a fruta para remover" )
entry_remover = tk.Entry()
entry_remover.grid()


tk_button_remover = tk.Button(text="remover",command= remover_frutas)
tk_button_remover.grid()

label_conjunto = tk.Label(text='   ')
label_conjunto.grid()





janela.geometry("600x400")
janela.config(bg="pink")
janela.title("Remover Frutas")
janela.mainloop()