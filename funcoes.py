#Funcções, Parâmetros, argss e kwargs

def soma_numeros(n1, n2):
    print(n1 + n2)

soma_numeros(5, 2)

soma_numeros(n1 = 5, n2 = 2)


def soma_numeros2(n1, n2, *args):
    print(f'n1 = {n1} n2 = {n2} args = {args}')
    
    
soma_numeros2(1, 2, 3, 4, 5, 6, 7, 8)


def soma_numeros3(*args):
    soma = 0
    for i in args:
        soma = soma + i
    print(soma)
    
    
soma_numeros3(1, 2, 3, 4, 5, 6, 7, 8)


def soma_numeros4(**kwargs):
    print(kwargs['teste1'])

soma_numeros4(teste1 = 1, teste2 = 2, teste3 = 3)    

def soma_numeros5 (**kwargs):
    x = kwargs.get('teste4')
    if x:
        print ('Foi passado!')
    else:
        print('Não foi passado')

soma_numeros5(teste1 = 1, teste = 2, teste3 = 3)

soma_numeros5(teste1 = 1, teste = 2, teste3 = 3, teste4 = 4)


#Retornando valores

def soma_valores (n1, n2):
    soma = n1 + n2
    if soma > 5:
        return soma
    print('TO AQUI')

soma = soma_valores(1, 2)
print(soma)
x = soma_valores(1, 2) + 1
print(x)

