
# from tkinter import simpledialog, messagebox, Button , Tk

# janela = Tk()

# def abrir_dialog():
#     open = simpledialog.askinteger("questão", "o que entendeu?")
#     if  open.strip() == 'entendi':
#         messagebox.showinfo('resultado', 'muito bem!')
#     else:
#         messagebox.showinfo('resultado', 'não entendeu ')

# btn = Button(text="dialong", command=abrir_dialog)
# btn.grid()

# janela.mainloop()
from tkinter import Tk, Button, Entry, Label

def numero_adicionar():
    try:
        x = int(entrada.get())
        resultado.config(text=f"Número válido: {x}")
    except ValueError:
        resultado.config(text="Ops! Esse não é um número válido. Tente novamente...")

janela = Tk()
janela.title("Número")

Label(janela, text="Insira um número:").pack(pady=5)

entrada = Entry(janela)
entrada.pack(pady=5)

Button(janela, text="Calcular valor", bg="lightblue", command=numero_adicionar).pack(pady=5)

resultado = Label(janela, text="")
resultado.pack(pady=5)

janela.mainloop()
