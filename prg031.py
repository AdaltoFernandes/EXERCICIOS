'''
prg031 - Escreva um programa que leia os valores da gasolina e do etanol de um determinado 
posto de abastecimento de combustível. Seu programa deve verificar e informar qual 
combustível é mais vantajoso para o cliente, considerando que o etanol rende 30% menos que 
a gasolina.
'''

gasolina = float(input('Digite o valor do litro da GASOLINA: '))
etanol = float(input('Digite o valor do litro do ETANOL: '))


if etanol < gasolina * 0.70:
    print('Abasteça com Etanol vale mais a pena')
else:
    if etanol == gasolina * 0.70:
        print('Tanto faz, pode abastecer o que preferir.')
    else:
        print('Abasteça Gasolina vale mais a pena.')



# if gasolina < etanol * 0.70:
#     print('Abasteça Gasolina, vale mais a pena')
# elif gasolina == etanol * 0.70:
#     print('Tanto faz, pode abastecer o que preferir.')
# else:
#     print('Abasteça Etanol, vale mais a pena.')