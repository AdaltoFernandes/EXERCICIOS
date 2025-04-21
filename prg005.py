# prg005 - Escreva um programa que leia o raio de uma esfera e informe o seu volume. Considere para seu cálculo o valor de π = 3,14159 - OLHAR SLIDE PARA TIRAR DUVIDA -> FORMULA 𝑉=43𝜋𝑟3
import math

raio = float(input('Digite o raio da esfera:'))

area = (4/3)*math.pi*raio**3

print(f'O volume da esfera é:{area}')