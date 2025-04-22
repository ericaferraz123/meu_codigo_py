import tkinter as tk
#Aqui estamos importando a biblioteca
# Tkinter para criar a interface gráfica
# . O tk é um apelido que usamos para
# facilitar o uso da biblioteca.

def mostrar_maior_menor():
    notas = []
    
    for entrada in [linha1, linha2, linha3, linha4, linha5, linha6]:
        valor = entrada.get()
        if not valor.replace('.', '', 1).isdigit():
            label_resultado.config(text="Por favor, insira apenas números válidos.")
#Função mostrar_maior_menor: Essa função é chamada quando o botão é pressionado.
# Ela vai buscar os valores das 6 caixas de entrada (onde o usuário digita as notas),
# verificando se são números válidos.

            return  
        notas.append(float(valor))
    
    maior = max(notas)
    menor = min(notas)

#Verificação do número: A função valor.replace('.', '', 1).isdigit()
# verifica se o valor inserido é um número válido. Ela permite que o número 
# tenha um ponto (para números decimais), mas não aceita letras
# ou caracteres inválidos.


    label_resultado.config(text=f"Maior Nota: {maior}, Menor Nota: {menor}")

janela = tk.Tk()
janela.title("Maior e Menor Nota")
#Define o título da janela (aparece na parte de cima da janela).
janela.config(background="#f5aecf")
janela.geometry("400x400")
#Define o tamanho inicial da janela para 400 pixels de largura e 400 pixels de altura.
janela.maxsize(width=1200, height=900)
janela.minsize(width=400, height=300)


label_instrucao = tk.Label(janela, text="Digite 6 notas:", fg="#ffffff", bg="#5f3999", font=("Slab", 12))
label_instrucao.pack()

linha1 = tk.Entry(janela)
linha1.pack(pady=5)
linha2 = tk.Entry(janela)
linha2.pack(pady=5)
linha3 = tk.Entry(janela)
linha3.pack(pady=5)
linha4 = tk.Entry(janela)
linha4.pack(pady=5)
linha5 = tk.Entry(janela)
linha5.pack(pady=5)
linha6 = tk.Entry(janela)
linha6.pack(pady=5)
#Aqui, são criadas 6 caixas de entrada (Entry)
# para o usuário digitar as 6 notas. A função pack() 
# coloca as caixas de entrada na janela e o pady=5 adiciona
# um pouco de espaço vertical entre elas.

novo_botao = tk.Button(janela, text="Mostrar Maior e Menor Nota", bg='#5f3999', fg='#d6cee0', command=mostrar_maior_menor)
novo_botao.pack(pady=10)
label_resultado = tk.Label(janela, text="Resultado", font=("Slab", 12), background="#c2a7bf")
label_resultado.pack()
janela.mainloop()
#(): Inicia o loop principal da janela.
# Isso significa que a janela vai ficar aberta e
# aguardando as interações do usuário (como clicar
# no botão ou digitar nas caixas de entrada).
