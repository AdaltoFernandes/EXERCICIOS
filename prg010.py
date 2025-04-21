""""
prg010 - Escreva um programa que converta uma temperatura digitada em °C em °F.
"""
# Usei virgula, não dava o resultado certo era como string, agora usando o ponto funcionou. 

celsius = float(input('Digite o valor em graus celsius:'))

calculo = celsius * 1.8 + 32

print(f'Esse é o valor em °F:{calculo}')