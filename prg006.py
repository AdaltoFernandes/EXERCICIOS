# prg006 - Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.
# 1 min = 60 segundos
# 1 hora / 60 min = 3.600 seg (60 * 60)
# 1 dia - 24h = 86.400 seg (24 * 3600)

dias = int(input('Dias:'))
horas = int(input('Horas:'))
minutos = int(input('Minutos:'))
segundos = int(input('Segundos:'))

total_em_segundos = dias * 24 * 3600 + horas * 3600 + minutos * 60 + segundos

print(f'O total em segundos é: {total_em_segundos} segundos.')