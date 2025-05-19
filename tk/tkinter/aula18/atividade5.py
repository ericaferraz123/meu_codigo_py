import tkinter as tk
janela= tk.Tk()
janela.title("tupla numero")
janela.config(bg="pink")
janela.geometry("600x400")
tupla_numero=(4,7,9,56)
soma=0
 
def soma_numeros():
    global soma
    for numero in tupla_numero:
        soma+= numero  
    label_numeros.config(text=soma)
    botao_numeros.config(state="disabled")
 
 
 
 
botao_numeros = tk.Button(janela, text="exiba a soma ",command=soma_numeros)
botao_numeros.pack(side="top")
 
label_numeros=tk.Label(janela,text="",bg="pink")
label_numeros.pack(side="top",pady=30,anchor="s")
janela.mainloop()
 