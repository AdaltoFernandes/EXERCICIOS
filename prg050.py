'''
prg050 - Escreva um programa que leia o nome e a as três notas de 6 alunos. Seu programa
deve calcular e informar a média ponderada, onde as notas têm os pesos 2, 3 e 5
respectivamente. Seu programa também deve informar o grau do aluno, aprovado para notas
maiores ou iguais a 6 e em recuperação para as notas menores que 6.
'''

for x in range (6):
    nome = input('Digite seu nome: ')
    n1 = float(input('Digite sua nota 1: ')) # peso 2
    n2 = float(input('Digite sua nota 2: ')) # peso 3
    n3 = float(input('Digite sua nota 3: ')) # peso 5
    print(f'O aluno {nome} tem as seguintes notas: {n1}, {n2} e {n3}.')
    # Calcular e informar a media ponderada, onde as notas tem os pesos 2, 3 e 5.
    mp = (n1*2 + n2*3 + n3*5) / 10
    # Informar o grau do aluno, aprovado para notas maiores ou iguais a 6 e em recuperação para as notas menores que 6.
    if mp < 6:
        print(f'O {nome} está de recuperação, porque sua nota é {mp}.')
    else: 
        print(f'O {nome} está aprovado e sua nota é {mp}')


