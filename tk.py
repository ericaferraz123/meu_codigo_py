#  atividade 1
# import tkinter as tk
 
 
# def pesquisar_restricao():
#     numero = lb_numero.get()  
#     numero = int(numero)
#     if numero in [1, 2]:
#         label_resultado.config(text="Não Circular 2ª Feira")
#     elif numero in [3, 4]:
#         label_resultado.config(text="Não Circular 3ª Feira")
#     elif numero in [5, 6]:
#         label_resultado.config(text="Não Circular 4ª Feira")
#     elif numero in [7, 8]:
#         label_resultado.config(text="Não Circular 5ª Feira")
#     elif numero in [9, 0]:
#         label_resultado.config(text="Não Circular 6ª Feira")
#     else:
#         label_resultado.config(text="Número inválido")
 
 
 
# janela = tk.Tk()
# janela.title("Restrição de Circulação")
# janela.config(background = "#619191")
# janela.geometry("400x300")
# janela.maxsize(width=1200, height=900)
# janela.minsize(width=400, height=200)
 
# label_instrucao = tk.Label(text="Digite o último número da placa do carro:", fg="white", bg="black", font=80 )
# label_instrucao.pack()
 
 
# lb_numero = tk.Entry(janela)
# lb_numero.pack()
 
 
# novo_botao = tk.Button(text='ENVIAR', bg='#b6c7d4', fg='#16598c', command= pesquisar_restricao)
# novo_botao.pack()
 
# label_resultado = tk.Label(janela, text="Resultado")
# label_resultado.pack()
 
# janela.mainloop()
#atividade2
import tkinter as tk
 
def calcular_total():
    prato_selecionado = entrada_escolha.get()
    gorjeta_ativa = gorjeta_var.get()
 
    # Preços dos pratos
    pratos = {
        "1": 80.0,
        "2": 25.0,
        "3": 70.0,
        "4": 20.0
    }
 
    if prato_selecionado in pratos:
        preco_prato = pratos[prato_selecionado]
        total = preco_prato
 
        if gorjeta_ativa:
            total *= 1.10
 
        total_label.config(text=f"Total a pagar: R${total:.2f}")
    else:
        total_label.config(text="Seleção inválida. Selecione um prato.")
 
def confirmar_escolha():
    prato_selecionado = entrada_escolha.get()
    if prato_selecionado in ["1", "2", "3", "4"]:
        prato_label.config(text=f"Você escolheu o prato {prato_selecionado}.")
        calcular_total()
    else:
        prato_label.config(text="Seleção inválida. Selecione um prato.")
 
janela = tk.Tk()
janela.title("Cardápio Interativo")
janela.geometry("300x350")
 
titulo_label = tk.Label(janela, text="Escolha seu prato", font=("Helvetica", 14))
titulo_label.pack(pady=10)
 
opcoes_pratos = tk.Label(janela, text="1-Pizza, 2-Hambúrguer, 3-Feijoada, 4-Macarronada")
opcoes_pratos.pack()
 
entrada_escolha = tk.Entry(janela)
entrada_escolha.pack()
 
novo_botao = tk.Button(janela, text="Confirmar escolha", command=confirmar_escolha)
novo_botao.pack(pady=5)
 
prato_label = tk.Label(janela, text="")
prato_label.pack()
 
gorjeta_var = tk.IntVar()  # Use IntVar para armazenar o estado do Checkbutton
gorjeta_checkbutton = tk.Checkbutton(janela, text="Gorjeta de 10%", variable=gorjeta_var)
gorjeta_checkbutton.pack()
 
calcular_button = tk.Button(janela, text="Calcular total", command=calcular_total)
calcular_button.pack(pady=5)
 
total_label = tk.Label(janela, text="Total a pagar: R$0.00", font=("Helvetica", 12))
total_label.pack(pady=20)
 
janela.mainloop()