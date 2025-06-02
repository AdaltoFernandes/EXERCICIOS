'''
prg049 - Escreva um programa que execute 5 operações de soma. Para cada operação o
programa deve pedir dois números e informar a soma com o seguinte formato: Soma 1 = 10,
onde o 1 do exemplo representa o número da soma e o 10 o resultado da adição dos dois
números informados.
'''

for x in range(5):
    a = int(input('Digite um número: '))
    b = int(input('Digite outro número: '))
    s = a + b
    print('Soma ', x+1 , ':' , s)

# Esse programa faz 5 vezes esse formato.
    