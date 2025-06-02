'''
Crie um programa que leia 100 números inteiros e ao final
informe qual foi o maior e qual foi o menor número lido.
'''
maior = 0
menor = 0
for x in range(100):
    num = int(input("Digite um número:"))
    if x==0 or num>maior:
        maior = num
    if x==0 or num<menor:
        menor = num
print("Maior:", maior)
print("Menor:", menor)

'''
prog_a -> Crie um programa que leia o salário de 15 funcionários. Ao
final informe o menor salário.
'''
menor = 0
for i in range(15):
    salario = float(input("Informe o salário:"))
    if i==0 or salario<menor:
        menor=salario
print("Menor salário:", menor)

'''
prog_b -> Crie um programa que leia o nome e a media de 20 
alunos. Seu programa deve informar o nome e a média do aluno
com maior média.
'''
maior = 0
for x in range(20):
    nome = input("Nome do aluno:")
    media = float(input("Média do aluno:"))
    if x==0 or media>maior:
        maior = media
        nome_maior = nome
print("*** Maior média ***")
print("Aluno:", nome_maior)
print("Média:", maior)

'''
proc_c -> Crie um programa que leia as idades de 500 pessoas para uma
pesquisa. Seu programa deve processar e informar:
a) a maior idade
b) a menor idade
c) a média das idades
d) a quantidade de pessoas com 18 anos ou menos
'''
maior, menor, soma, qtde = 0, 0, 0, 0
for x in range(500):
    idade = int(input("Informe a idade:"))
    if x==0 or idade>maior:
        maior = idade
    if x==0 or idade<menor:
        menor = idade
    soma += idade
    if idade<=18:
        qtde += 1
print("*** Resultado ***")
print("a)", maior)
print("b)", menor)
print("c)", soma/500)
print("d)", qtde)
