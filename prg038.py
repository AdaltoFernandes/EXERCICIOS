'''
prg038 - Escreva um programa que leia uma idade (número inteiro) e se é brasileiro (True ou
False). Ao final deve informar:
• Idade de 18 a 70 anos e brasileiro........................................... : Voto obrigatório
• Idade de 16 a 17 ou acima de 70 anos e brasileiro.................. : Voto não obrigatório
• Abaixo de 16 anos ou não brasileira........................................ : Voto não permitido

'''

idade = int(input('Digite sua idade: '))
brasileiro = bool(input('Voce é Brasileiro True ou False:'))

if brasileiro== False or idade<16:
    print('Voto não permitido.')
else:
    if idade>=18 and idade<=70:
        print('Voto Obrigatorio.')
    else:
        print('Voto não obrigatorio.')