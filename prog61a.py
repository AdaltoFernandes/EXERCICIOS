'''
Crie um programa que leia um numero int e informe se ele é ou não é primo.
Obs.: O número primo é aquele qe só tem divisões exatas por 1 e por ele mesmo.
'''
# Pegando numero primo até 1000.

# Fale os 100 primeiros numeros primos. 

num = 2
for num in range(1, 10000):
    count = 0
    for x in range(1, num+1):
         if num % x ==0:
             count += 1
    if count == 100:
        print(f'{num}')
        print('Kitkat')
        break

# Pegando numero primo até 1000.
# num = int(input('Digite um número: '))
# for num in range(2, 1000):
#     count = 0
#     for x in range(1, num+1):
#         if num % x ==0:
#             count += 1
#     if count == 2:
#         print(f'{num} é primo!')
#     else: 
#         print(f'{num} não é primo')

####### Diz se é numero primo o não
# count = 0
# num = int(input('Digite um número: '))

# for x in range(1, num+1):
#     if num % x ==0:
#         count += 1
# if count == 2:
#     print(f'{num} é primo!')
# else: 
#     print(f'{num} não é primo')