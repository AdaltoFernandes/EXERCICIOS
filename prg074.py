'''
Escreva um programa que leia um CPF e informe se é um CPF válido ou não. Caso não 
seja  um  CPF  válido  informe  este  fato  ao  usuário  e  pergunte  se  quer  finalizar  ou  tentar 
novamente. 
Obs.: Pesquise a regra para validação do CPF na Internet.
'''

valido = True
cpf = input('Digite um cpf sem o traço: ')
s = 0 
for x in range(9):
    s += int(cpf[x])*(9-x+1)
    print("%d x %d = %d" % (int(cpf[x]),9-x+1, int(cpf[x])*(9-x+1)))
if s% 11<=1:
    dv1 = 0
else:
    dv1 = 11 - s%11
if dv1!=int(cpf[9]):
    valido = False
# Verificar ainda o dv2

if valido ==True:
    
    print('CPF Válido!')
else:
    print('CPF Inválido.')


