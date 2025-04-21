''' prg008 - Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.

aumento = salario_atual * (aumento_porcentagem / 100)
total = aumento + salario_atual
'''
mercadoria = float(input('Digite o valor da mercadoria:'))
inp_desconto = float(input('Digite o valor do desconto:'))

desconto = mercadoria * (inp_desconto / 100)
total = mercadoria - desconto

print(f'Esse é o valor do desconto: {desconto} reais, o preço a se pagar com desconto é de:{total} reais')

