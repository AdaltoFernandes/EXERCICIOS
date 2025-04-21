'''prg011 - Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.
'''
# Pergunta de KM percorrido.
# Pergunta a quantidade dias que o caro foi alugado.

km_percorrido = float(input('Digite o KM percorrido:'))
quantidade_dias = float(input('Digite a quantidade de dias que carro foi alugado:'))

calculo = (km_percorrido * 0.15) + (quantidade_dias * 60)

print(f'O valor é total é de R${calculo}')
print('O total a pagar é de R${:.2F}'.format(calculo)) # feito pelo guanabara.

