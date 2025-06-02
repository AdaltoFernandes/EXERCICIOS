'''
Escreva um programa que leia uma letra e caso a letra seja C, imprima "Casado", caso S "Solteiro",  e caso não seja nenhuma das duas, imprima "Estado Civil não encontrado."
'''
letra = input('Digite a Letra do seu Estado Civil "S" OU "C":')

# if letra == 'S':
#     print('Solteiro')
# elif letra == 's':
#     print('Solteiro')
# elif letra == 'C':
#     print('Casado')
# elif letra == 'c':
#     print('Casado')
# else:
    
if letra == 'S' or letra == 's':
    print('Solteiro')
elif letra == 'C' or letra == 'c':
    print('Casado')
else:
    print('Estado Civil não encontrado!')