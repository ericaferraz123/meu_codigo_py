#atividade 1
# largura = int(input('Digite a largura: '))
# altura = int(input('Digite a altura: '))
# if altura == largura:
#     print("altura e largura são iguais.")
# else:
#     for i in range(largura):
#         for j in range(altura):
#            print("*", end='')
#     print()
# #atividade2
for i in range(1, 11):
    for j in range(1, 11):  
        print(f"{i} x {j} = {i * j}")  
    print("-" * 15)
 
#atividade 3
n = int(input("Digite um número: "))  
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
#atividade 4
for i in range(8):  
    for j in range(8):  
        if (i + j) % 2 == 0:
            print("#", end=" ")
        else:
            print(" ", end=" ")
    print()
 
#atividade 5
num = 1
for i in range(5):  
    for j in range(5):  
        print(f"{num:2}", end=" ")
        num += 1  
    print()  