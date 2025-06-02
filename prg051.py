'''
prg051 – Escreva um programa que leia a temperatura inicial de um motor e quantos graus ela
ganha a cada leitura de 10 segundos, por fim calcule e informe quantos graus ela terá após 16
leituras.
'''

temp_i = float(input('Digite a temperatura inicial do motor: '))
for x in range (15):
    temp_10 = float(input('Digite o valor que aumentou em 10seg'))
    # A variavel temp_i vai guardando o primeiro resultado e somando cada loop no total.
    temp_i += temp_10
print(f'A temperatura final do motor é de {temp_i}')
