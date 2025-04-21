"""
prg012 - Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro, e calcule quantos dias de vida um fumante perderá. Exiba o total em dias.
"""
# Pergunte a quantidade de cigarros fumados por dia.
# Pergunte quantos anos ele já fumou.
# Considere que 1 cigarro é -10 minutos de vida.
# Calcule quantos dias de vida um fumante perderá.
# Exiba o total em dias. 
# 1min = 60 seg - 10 min = 600seg


cigarros_dia = int(input('Quantos cigarros voce fuma por dia?'))
anos_fuma = float(input('A quantos anos voce fuma?'))

cigarros_minuto = (anos_fuma * 365)* (cigarros_dia*10)
cigarro_dia_total = cigarros_minuto/(24*60)

#Forma que eu aprendi, dentro fstring usando o :.2f
print(f'Voce perdeu {cigarro_dia_total:.2f} de vida')
# Essa forma abaixo é que funciona para formatar.
print('Voce perdeu {:.2f} dias de vida por fumar cigarro.'.format(cigarro_dia_total))
print('Devido ao tabagismo voce perdeu {:.2F} dias'.format(cigarro_dia_total))