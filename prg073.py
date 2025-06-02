'''
Escreva  um  programa  que  leia  um  endereço  de  email e  verifique  se  é  um endereço 
de e-mail válido. Um endereço de email válido deve conter pelo menos 10 caracteres, sendo 1 
deles (somente um) um ponto e um arrouba. Este arrouba e este ponto não podem estar nem 
no  início  e  nem  no  final  da  cadeia  lida.  Caso  não  seja  um  email  válido  informe  este  fato  ao 
usuário e pergunte se quer finalizar ou tentar novamente.
'''

continua='s'
while continua =='s':
    valido = True
    email = input("Informe seu e-mail:")
    if len(email)<10:
        valido = False
    else:
        if email[0] == "." or email[0]== '@' or email[len(email)-1]=="." or email[len(email)-1] =='@':
            valido = False
        else:
            count=0
            for x in range(len(email)):
                if email[x]== '@':
                    count += 1
            if count!=1:
                valido = False
    if valido==True:
        print('É um email válido')
    else:
        print('Não é um email válido!')
continua = input('Deseja continuar verificando emails? <s/n>')
print('fim')

