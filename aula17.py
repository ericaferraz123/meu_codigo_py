# fila = []
 
# while True:
#     print("\n1 - Adicionar cliente")
#     print("2  - Atender cliente")
#     print("3 -  Ver fila")
#     print("4  - Sair")
    
#     opcao = input("Escolha uma opção: ")
    
#     if opcao == "1":
#         nome = input("Nome do cliente: ")
#         fila.append(nome)
#         print(f"{nome} entrou na fila.")
        
#     elif opcao == "2":
#         if fila:
#             atendido = fila.pop(0)
#             print(f" {atendido} foi atendido.")
        
#     else:
        
#         print("Fila vazia!")
    
#     elif opcao == "3":
#         print("Fila atual:", fila)
#     elif opcao == "4":
#         break
#     else:
#          print("Opção inválida.")


def fila_tarefas():
    fila = []
    while True:
        print("\nOpções de Fila de Tarefas:")
        print("1. Adicionar tarefa")
        print("2. Remover tarefa (Atender)")
        print("3. Visualizar fila")
        print("4. Voltar ao menu principal")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            tarefa = input("Digite a tarefa para adicionar: ")
            fila.append(tarefa)
            print(f"Tarefa '{tarefa}' foi adicionada à fila.")
        elif opcao == '2':
            if fila:
                tarefa_atendida = fila.pop(0)
                print(f"A tarefa '{tarefa_atendida}' foi atendida e removida da fila. Restam {len(fila)} tarefas.")
            else:
                print("A fila está vazia!")
        elif opcao == '3':
            if fila:
                print("\nFila de Tarefas:")
                for i, tarefa in enumerate(fila, 1):
                    print(f"{i}. {tarefa}")
            else:
                print("A fila está vazia!")
        elif opcao == '4':
            break
        else:
            print("Opção inválida.")