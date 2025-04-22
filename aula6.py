# atividade 1
# numero = int (input('Digite um número:'))
# for num in range(10,numero,2):
#     print(num)
#atividade 2
# numero = int(input("Digite um número para ver a tabuada: "))
 
# print(f"Tabuada de: {numero}")
# for i in range(1, 11):
#         resultado = numero * i
# #         print(f"{numero} * {i} = {resultado}")
# # atividade 3
# for i in range(10,0,-1):
#     print(i)
# print("FIM")
# #atividade 4
# soma = 0
# for i in range (0,5):
#     soma += int(input("Digite o numero: "))
# print(f"O resultado :{soma}")
 
 
#atividade 5
palavra = input("digite uma palavra: ")
vogais = "aeiou AEIOU"
contagem_de_vogais = 0
 
for letra in palavra:
    if letra in vogais:
        contagem_de_vogais += 1
print(f"a quantidade de vogais na  {palavra} e: {contagem_de_vogais} ")