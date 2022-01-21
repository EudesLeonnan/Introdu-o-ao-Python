"""Faça um programa que o usuário possa cadastrar n pessoas,
armazenando seu nome, idade e altura"""


pessoas = []
while True:
    decisao = int(input('Digite 1 para cadastrar uma pessoa, ou digite 2 para sair  '))
    if decisao == 2:
        break
    elif decisao == 1:
        pessoas.append({'nome': input('Digite o nome da pessoa:  ') ,  
                        'idade': input('Digite a idade da pessoa:  '), 
                        'altura': input('Digite a altura da pessoa:  ') })
    else:
        print('Valor inválido')
print(pessoas)

for pessoa in pessoas:
    print(pessoa['nome'], 'tem', pessoa['idade'],  'anos e', pessoa['altura'],'m de altura')



#Outra possibilidade

pessoas = []
while True:
    decisao = int(input('Digite 1 para cadastrar uma pessoa, ou digite 2 para sair  '))
    if decisao == 2:
        break
    elif decisao == 1:
        nome = input('Digite o nome da pessoa:  ')
        idade = input('Digite a idade da pessoa:  ')
        altura = input('Digite a altura da pessoa:  ')
        pessoa = {'nome': nome, 'idade': idade, 'altura': altura}
        pessoas.append(pessoa)
    else:
        print('Valor inválido')
for pessoa in pessoas:
    print(pessoa['nome'], 'tem', pessoa['idade'],  'anos e', pessoa['altura'],'m de altura')