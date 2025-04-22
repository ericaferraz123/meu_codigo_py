#atividade1 
# n = int(input("Digite um número inteiro N: "))
# a, b = 0, 1
# for i in range(n):
#     print(a, end=" ")
#     a, b = b, a + b

# #atividade 2
# for i in range(1, 31):
#     if i % 3 == 0:
#         print(i)

# #atividade3
# # impares = [i for i in range(1, 51) if i % 2 != 0]
# soma_impares = sum(impares)
# print(soma_impares)
# atividade 4
# frase = input("Digite uma frase: ")

# letras = 0
# for char in frase:
#     if char.isalpha():  
#         letras += 1

# print("A frase possui", letras, "letras.")
#atividade 5 
# def verifica_primo(n):
#     if n <= 1:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
# n = int(input("Digite um número para verificar se é primo: "))

# if verifica_primo(n):
#     print(f"{n} é primo.")
# else:
#     print(f"{n} não é primo.")
#atividade 6 
# quantidade = int(input("Quantos números você quer digitar? "))

# soma = 0

# for i in range(quantidade):
#     numero = float(input(f"Digite o {i + 1}º número: "))
#     soma += numero

# media = soma / quantidade

# print(f"A média dos números é: {media}")

# #atividade 7 
# palavra = input("Digite uma palavra: ")
# # print("A palavra ao contrário é:", palavra[::-1])

# #atividade8 
# numeros = []
# for i in range(5):
#     numero = int(input(f"Digite o {i + 1}º número: "))
#     numeros.append(numero)
# maior = max(numeros)
# print("O maior número digitado foi:", maior)
# # atividade 9
# palavra = input("Digite uma palavra: ")
# letra = input("Digite uma letra: ")
# contagem = palavra.count(letra)
# print(f"A letra '{letra}' aparece {contagem} vezes na palavra '{palavra}'.")
# # atividade 10
# n = int(input("Digite um número N: "))

# for i in range(1, n + 1):
#     print('*' * i)
