'''
prg028 - Escreva um programa que leia o nome, gênero e estado civil de uma pessoa. Caso a 
pessoa seja casada e do gênero “F”, peça também o tempo do casamento em anos. 
'''

nome = input('Digite seu Nome:')
genero = input('Digite seu Genero: "f" para Feminino ou "m" para Masculino.')
casada = input('Voce é casado(a)?: "s" para Sim ou "n" para Não.')
if genero == "f" and casada == "s":
    tempo_casamento = int(input('Digite seu tempo de casamento em anos:'))
    print(f'Olá {nome}, voce é {genero} ou seja mulher e está a {tempo_casamento} casada.')
else:
    print('Obrigado')
    
    