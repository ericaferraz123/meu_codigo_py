import tkinter as tk

janela = tk.Tk()

curso_a = set()
curso_b = set()

def add_a():
    nome = entrada_a.get()
    curso_a.add(nome)
    mostrar_resultado()

def add_b():
    nome = entrada_b.get()
    curso_b.add(nome)
    mostrar_resultado()

def mostrar_resultado():
    label_a.config(text=f"Curso A: {curso_a}")
    label_b.config(text=f"Curso B: {curso_b}")
    ambos = curso_a & curso_b
    so_a = curso_a - curso_b
    so_b = curso_b - curso_a
    label_ambos.config(text=f"Ambos: {ambos}")
    label_exclusivos.config(text=f"Só A: {so_a} | Só B: {so_b}")

tk.Label(text="Aluno Curso A:").grid(row=0, column=0)
entrada_a = tk.Entry()
entrada_a.grid(row=0, column=1)
tk.Button(text="Adicionar A", command=add_a).grid(row=0, column=2)

tk.Label(text="Aluno Curso B:").grid(row=1, column=0)
entrada_b = tk.Entry()
entrada_b.grid(row=1, column=1)
tk.Button(text="Adicionar B", command=add_b).grid(row=1, column=2)

label_a = tk.Label(text="Curso A: {}")
label_a.grid(row=2, column=0, columnspan=3)

label_b = tk.Label(text="Curso B: {}")
label_b.grid(row=3, column=0, columnspan=3)

label_ambos = tk.Label(text="Ambos: {}")
label_ambos.grid(row=4, column=0, columnspan=3)

label_exclusivos = tk.Label(text="Só A: {} | Só B: {}")
label_exclusivos.grid(row=5, column=0, columnspan=3)

janela.geometry("600x300")
janela.title("Cursos de Alunos")
janela.config(bg="purple")
janela.mainloop()
