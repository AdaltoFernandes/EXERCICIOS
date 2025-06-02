'''
prg029 - Escreva um programa que 3 números inteiros quaisquer. Seu programa deve informar 
estes números em ordem crescente. 
'''
# n1 = int(input('Digite o primeiro numero:'))
# n2 = int(input('Digite o segundo numero:'))
# n3 = int(input('Digite o terceiro numero:'))
# if n1 > n2 and n1 > n3:
#     print(f'Aqui o {n1} é maior')
# else:
#     if n2 > 
#     # print(f'O Maior numero é o primeiro numero ele é:{n1}.')
# else:
#     if n2 > n3:
#         print()
        
        
##
n1 = int(input('Digite o primeiro numero:'))
n2 = int(input('Digite o segundo numero:'))
n3 = int(input('Digite o terceiro numero:'))

# Confirma se n2 é maior que n1. 
if n2<n1:
    n2, n1 = n1 , n2 # se for ele troca o valor de n2 e joga em
if n3<n2:
    n3, n2 = n2, n3
if n2<n1:
    n2, n1 = n1, n2
# if n2>n1:
#     n1, n2 = n2, n1
    
     
print(n1, n2, n3)

####Essa forma é a decrescente.
# Confirma se n1 é maior que n2. 
# if n2<n1:
#     # Se n2 for maior ele troca o valor do n2 para n1. 
#     n2, n1 = n1 , n2 
# # Confirma se n3 é maior que n2.
# if n3<n2:
#     # Se n3 for maior ele troca o valor de n3 para n2.
#     n3, n2 = n2, n3
# # Confirma se n2 é maior que n1.
# if n2<n1:
#     # Se n2 maior que n1 ele troca o valor de n2
#     n2, n1 = n1, n2
        
        
# print (n1, n2, n3)
    