# prg009 - Escreva um programa que calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.

distancia = float(input('Digite a distancia da viagem:'))
vel_med = float(input('Digite a velocidade média da viagem:'))

# Distancia dividido pela velocidade média é o tempo.
calculo = distancia / vel_med

print(f'O tempo de viagem é de {calculo} hora')

