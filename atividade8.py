def calcular_pontos(num_livros):
 

 
if num_livros == 0:
 
return 0
 
elif num_livros == 1:
 
return 5
 
elif num_livros == 2:
 
return 15
 
elif num_livros == 3:
 
return 30
 
else:
 
return 60
 
def escolher_brinde (pontos):
 
"""Determina o brinde que o cliente pode escolher com base em seus pontos."""
 
if 20 <= pontos <= 30:
 
return "EcoBag OU Caneta personalizada"
 
elif 35 <= pontos <= 60:
 
return "Um livro (com valor máximo de R$ 30,00) Ου Luminária de cabeceira"
 
elif pontos >= 65:
 
return "2 livros (com valor máximo de R$ 100,00) Ου Powerbank"
 
else:
 
return "Nenhum brinde disponível"
 
# Exemplo de uso
 
num_livros = int(input("Digite o número de livros comprados: "))
 
pontos = calcular_pontos (num_livros)
 
brinde escolher_brinde (pontos)
 
print(f"Pontos: {pontos}")
 
print(f"Brinde: {brinde}")