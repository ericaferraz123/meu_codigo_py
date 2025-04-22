# Crie um programa que solicite um número
# inteiro ao usuário e informe se ele é par ou ímpar.
# (lembre-se do casting para int(...)) 
# (o úmero divisivel por 0 é par - numero % 2 == 0)
# num = int(input('Digite o número:'))
# if num % 2 == 0 :
#     print("O número é par ")
# else:
#     print("O número é impar ")

#atividade 2 
# num1 = float(input("Digite o número 1 : "))
# num2 = float(input("Digite o número 2 : "))
# if num1 > num2 :
#     print(f'Número maior {num1}')
# elif num2 > num1 :
#     print(f'Número menor {num1} ')
# else :
#     print("Números iguais.")
#atividade 3

# valor_inicial = input("Digite o valor das suas compras para verificar descontos: ")
# if(float(valor_inicial) >= 100.00):
#     desconto = float(valor_inicial) * 0.10
#     valor_total = float(valor_inicial) - desconto
#     print(f"O valor com os descontos é de: {valor_total}")
# elif(float(valor_inicial) >= 50.00):
#     desconto = float(valor_inicial) * 0.05
#     valor_total = float(valor_inicial) - desconto
#     print(f"O valor com os descontos é de: {valor_total}")
# else:
#     print(f"Não foi possivel encontrar descontos disponiveis o valor é de: {valor_inicial}")

#atividade 4 
# idade = int(input('Digite sua idade: '))
# if idade >= 18 :  
#     print('Maior de idade')
# else : 
#     print('Menor de idade ')
#atividade 5 
# num = float (input("Digite o número: "))
# if num >= 0: 
#     print("Número positivo.")
# elif num <= 0:
#     print("Número negativo. ")
# else: 
#     print("O número é zero. ")
#atividade 6

# nota1 = float(input("Digite a primeira nota: "))
# nota2 = float(input("Digite a segunda nota: "))

# media = (nota1 + nota2) / 2
# if media >= 7:
#     print("Aprovado")
# elif 5 <= media < 7:
#     print("Recuperação")
# else:
#     print("Reprovado")
# #atividade 7
# num1 = float(input("Digite o primeiro número: "))
# num2 = float(input("Digite o segundo número: "))
# operacao = input("Digite a operação (+, -, *, /): ")

# if operacao == "+":
#     resultado = num1 + num2
# elif operacao == "-":
#     resultado = num1 - num2
# elif operacao == "*":
#     resultado = num1 * num2
# elif operacao == "/":
#     if num2 == 0:
#         print(f"{resultado} = Não é possível dividir por zero.")
#     else:
#         resultado = num1 / num2 
        
# else:
#     print("Operação invalida ")
     
# print(f"Seu resultado é {resultado}. ")
#atividade 8 
# lado1 = input("Digite o primeiro lado: ")
# lado2 = input("Digite o segundo lado: ")
# lado3 = input("Digite o terceiro lado: ")
# if lado1 == lado2 == lado3 :
#     print("Triângulo Equilátero")
# elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3 :
#     print("Triângulo Isósceles")
# else: 
#     print("Triângulo Escaleno")
#atividade 9 número multiplo 
# num1 = int(input("Digite o primeiro número: "))
# num2 = int(input("Digite o segundo número: "))
 
# if num2 != 0 and num1 % num2 == 0:
#     print(f"{num1} é múltiplo de {num2}")
# else:
#     print(f"{num1} não é múltiplo de {num2}")
#atividade 10 
graus_c = input("Informe o graus em celcios para a converção: ")
covercao = input("Informe para qual você vai converter (F) para fahrenheit e (K) para kelvin: ")
if(covercao == "F" or covercao == "f" ):
    calculo = float(graus_c) * 1.8 + 32
    print(f"A temperatura em Fahrenheit é de: {calculo}")
elif(covercao == "K" or covercao == "f" ):
    calculo = float(graus_c) + 273.15
    print(f"A temperatura em Kelvin é de: {calculo}")
 