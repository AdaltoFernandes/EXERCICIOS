'''
prg030 - Escreva um programa que leia o nome e o preço de três produtos e informe qual 
produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
'''

p1_nome = input('Digite o nome do primeiro produto')
p1_preco = float(input('Digite o valor do produto:'))
p2_nome = input('Digite o nome do segundo produto')
p2_preco = float(input('Digite o valor do produto:'))
p3_nome = input('Digite o nome do terceiro produto')
p3_preco = float(input('Digite o valor do produto:'))

if p1_preco < p2_preco and p1_preco < p3_preco:
    print(f'O produto {p1_nome} com o preço de {p1_preco} é o mais barato')
else:
    if p2_preco < p3_preco and p2_preco < p1_preco:
        print(f'O produto {p2_nome} com o preço de {p2_preco} é o mais barato')
    else:
        print(f'O produto {p3_nome} com o preço de {p3_preco} é o mais barato')