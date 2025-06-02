'''
prg026 - Escreva um programa para a leitura de duas notas de um aluno. O programa deve 
calcular a média alcançada pelo aluno e apresentar:  
• A mensagem "Aprovado", se a média alcançada for maior ou igual a seis;  
• A mensagem "Reprovado", se a média for menor do que seis;  
• A mensagem "Aprovado com Distinção", se a média for igual a dez. 
'''
media = float(input('Digite sua média:'))

if media >= 6:
    print('Aprovado!')
else:
    if media >= 3:
        print('Recuperação')
    else: 
        print('Reprovado')
               
# if media >=6:
#     print('Aprovado')
# elif media >=3:
#     print('Recuperação')
# else:
#     print('Reprovado')