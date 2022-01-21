#Receba 10 valores e exiba a soma de todos eles

valores = []
x = 0
for i in range(0,10):
    x += int(input(f'Digite o valor {i+1}:  '))
print(f'A soma é: {x}')

#for i in range(0,10):
#    x = [int(input(f'Digite o valor {i+1}:  '))]
#print(f'A soma é: {x}')

x = [int(input(f'Digite o valor {i+1}:  ')) for i in range(0,10)]
soma = 0
for i in x:
    soma = soma + i
print(f'A soma é: {soma}')