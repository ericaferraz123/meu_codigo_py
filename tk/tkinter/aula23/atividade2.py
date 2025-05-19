# criar um cárdapio com pratos com preços
#permitir qu eo usuário escolha um prato e exiba o preço 

cardapio = {
    "pizza": 35,
    "hambúrguer": 15,
    "churrasco": 50,
    "carreteiro": 45,
    "macarrão": 25
}

print(" Aqui esta o valor do prato:")
for prato in cardapio:
    print(f" {prato}: R$ {cardapio[prato]}")
escolha = input(" Qual prato vc deseja? ").lower().strip()

if escolha in cardapio:
    print(f" O preço de {escolha} é R$ {cardapio[escolha]}.")
else:
    print(" Não temos esse prato no cardápio. ")





#.lower().sprip()