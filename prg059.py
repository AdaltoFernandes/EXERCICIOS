'''
Escreva um programa que leia o nome e o peso em kg que diversos atletas estrão levantando em uma competição.
Seu programa deve finalizar qando o nome "fim" for digitado no nome e informar o nome do medalista de ouro.
'''
# Para o programa quando o nome for fim.
while True:
    nome = input('Digite o nome:')

    if nome == 'fim':
        break
    peso = input('Digite o peso levantado: ')
