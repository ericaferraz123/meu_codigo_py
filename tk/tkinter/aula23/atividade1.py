#criar um dicionário com nome e nota de 3 alunos.
#  exibir quem foi aprovado (nota>=7)
alunos = {}
for i in range(3):
    nome = input("Digite o Nome: ")
    nota = float(input("Digite sua nota: "))
    alunos[nome] = nota 

for nome, nota in alunos.items():
    if nota >= 7:
        print(f"{nome} passou com a nota de aprovamento: {nota}")
    else:
        print(f"{nome} não conseguiu passar com a nota: {nota}")


