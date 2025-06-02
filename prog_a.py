'''
Prog_a -> Crie um programa que leia o salario de 15 funcionarios. Ao final infomre o menor salário.

Prog_b -> Crie um programa que leia o nome de 20 alunos. Seu programa deve informar o nome e a média do aluno com amior média.

Prog_c -> Crie um programa que leia as idades de 500 pessoas para uma pesquisa. Seu programa deve processar e informar:
a) A maior idade
b) A menor idade 
c) a média das idades
d) a quantidade de pessoas com 18 anos ou menos
'''
# PROG A
salario_menor = 0
for x in range(15):
    salario = float(input('Digite o seu salario: '))
    if  x==0 or salario<salario_menor:
        salario_menor = salario

print(f'O menor numero de salario é {salario_menor}')


# PROG B
maior = 0
for x in range(20):
    nome = input('nome do aluno')
    media = float(input('Digite sua média'))




# PROG_C
maior, menor, soma, qtde = 0, 0, 0, 0
for x in range(500):