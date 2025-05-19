import tkinter as tk

janela = tk.Tk()

fila = []


def adicionar_tarefa():
    tarefa = entrada.get()
    if tarefa:
        fila.append(tarefa)
        resultado_label.config(text=f"Tarefa '{tarefa}' foi adicionada à fila.")
    else:
        resultado_label.config(text="Por favor, digite uma tarefa.")


def pesquisar_na_fila():
    tarefa = entrada.get()
    if tarefa in fila:
        resultado_label.config(text=f"Tarefa '{tarefa}' está na fila.")
    else:
        resultado_label.config(text=f"Tarefa '{tarefa}' não encontrada na fila.")
    entrada.delete(0, tk.END)


janela.title("Gerenciador de Filas")
janela.config(background="pink")
janela.geometry("600x400")


entrada = tk.Entry(janela)
entrada.pack(pady=10)



adicionar_button = tk.Button(janela, text="Adicionar Tarefa", command=adicionar_tarefa)
adicionar_button.pack(pady=5)

pesquisar_button = tk.Button(janela, text="Pesquisar Tarefa na Fila", command=pesquisar_na_fila)
pesquisar_button.pack(pady=5)


resultado_label = tk.Label(janela, text="", bg="pink")
resultado_label.pack(pady=20)


janela.mainloop()
