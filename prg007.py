# prg007 - Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.

salario_atual = float(input('Digite o valor do seu salario atual:'))
aumento_porcentagem = float(input('Digite a porcentagem do aumento:'))

aumento = salario_atual * (aumento_porcentagem / 100)
total = aumento + salario_atual


print(f'O valor do aumento é: {aumento} do novo salario é {total}')