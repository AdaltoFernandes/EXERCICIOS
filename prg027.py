'''
prg027 - Escreva um programa baseado no prg026, mas inclua na leitura o percentual de 
frequência do aluno. Se o aluno obtiver um percentual menor que 75, estará reprovado não 
importando a sua média. 
'''
media = float(input('Digite sua média:'))
frequencia = float(input('Digite a porcentagem de sua frequencia:'))

if frequencia < 75:
    print('Reprovado')
else:
    if media >= 6:
        print('Aprovado!')
    else:
        if media >= 3:
            print('Recuperação')
        else: 
            print('Reprovado')
            
####
# if frequencia < 75:
#     print('Reprovado')
# elif media >= 6:
#         print('Aprovado!')
# elif media >= 3:
#         print('Recuperação')
#    else: 
#         print('Reprovado')
        