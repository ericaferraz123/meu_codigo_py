from tkinter import *
from tkinter import simpledialog, messagebox

janela_principal = Tk()
janela_principal.geometry('400x350+10+10')
janela_principal.title("Fila de Tarefas")

fila_tarefas = []

def atualizar_lista_tarefas():
    lista_tarefas_widget.delete(0, END)
    for tarefa in fila_tarefas:
        lista_tarefas_widget.insert(END, tarefa)

def add_tarefa():
    tarefa = simpledialog.askstring('Nova tarefa', 'Descrição da tarefa:')
    if tarefa:
        fila_tarefas.append(tarefa)
        atualizar_lista_tarefas()

def atender_tarefa():
    if fila_tarefas:
        tarefa_atendida = fila_tarefas.pop(0)
        atualizar_lista_tarefas()
        messagebox.showinfo("Tarefa Atendida", f"Tarefa '{tarefa_atendida}' atendida. Restam {len(fila_tarefas)} tarefa(s) na fila.")
    else:
        messagebox.showinfo("Fila Vazia", "Não há tarefas para atender.")

label_fila_titulo = Label(janela_principal, text='Tarefas na fila', font=('Arial', 12, 'bold'), anchor='w')
label_fila_titulo.pack(padx=20, anchor='w')

lista_tarefas_widget = Listbox(janela_principal, font=('Helvetica', 12))
lista_tarefas_widget.pack(pady=10, padx=20, fill='both', expand=True)

btn_adicionar_tarefa = Button(janela_principal, text='Adicionar Tarefa'.upper(), bg='black', fg='white', font=('Helvetica', 12, 'bold'), command=add_tarefa)
btn_adicionar_tarefa.pack(pady=5)

btn_atender_tarefa = Button(janela_principal, text='Atender Próxima Tarefa'.upper(), bg='green', fg='white', font=('Helvetica', 12, 'bold'), command=atender_tarefa)
btn_atender_tarefa.pack(pady=5)

janela_principal.mainloop()