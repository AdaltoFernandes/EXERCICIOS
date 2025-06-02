'''
Crie um programa que leia 100 numeros inteiros e ao final infrome qual foi o maior e qual foi o menor nuúmero.
'''

maior = 0
menor = 0
for x in range(100):
    num = int(input('Digite um número: '))
    if x==0 or num>maior:
        maior = num
    if x==0 or num<menor:
        menor = num
print(f'Maior {maior}')
print(f'Menor {menor}')

