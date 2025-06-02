cont = 0
acum = 0 
for x in range(100):
    idade = int(input('Digite a idade: '))
    acum = acum + idade    
    if idade>50:
        cont = cont + 1
