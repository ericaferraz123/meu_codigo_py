#Crie uma fila com 5 nomes. Mostre a fila e depois remova o primeiro nome (simulando atendimento).


from tkinter import *

janela = Tk()
janela.geometry('900x600+10+10')
janela.title("Fila de pessoas")
# janela.config(background='black', highlightbackground='green')

fila = ['Pessoa1','Pessoa2','Pessoa3','Pessoa4','Pessoa5',]

def atender():
    if fila:
        atendido = fila.pop(0)
        lb_atendido.config(text=atendido)
    else:
        lb_atendido.config(text='Fila está vazia')
        

for pessoa in fila:
    lb = Label(text=pessoa, font=50).pack(side='top', anchor='w', padx=50, pady=(50,0))
    
bt_atender = Button(text='ATENDER', bg='black', fg='white', font=('Helvetica', 12, 'bold'), command=atender)
bt_atender.pack(ipadx=15, ipady=15)

lb_atendido = Label(text='', font=50)
lb_atendido.pack(side='top', anchor='w', padx=50, pady=(50,0))

janela.mainloop()