'''
== IGUAL
!= DIFERENTE
> MAIOR QUE 
< MENOR QUE
>= MAIOR OU IGUAL
<= MENOR OU IGUAL
'''
nome = input('Digite o nome do aluno:')
n1 = float(input('Digite a primeira nota'))
n2 = float(input('Digite a segunda nota'))
media = (n1 +n2)/2
print(f'A média do aluno é {media:.1f}')
print('A média do aluno é %1.1f' % media)

if media >= 6:
    print('O aluno está Aprovado!')
if media <6:
    print('O aluno está de recuperação')
    
    # melhor forma com condição.
if media >= 6:
    print('O aluno esta aprovado.')
else:
    print('O aluno esta de recuperação')
    