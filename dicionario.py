x = { 'nomes': 'Eudes Leonnan', 'idades': 34, 'alturas': 1.70 }

print(x)
print(x['nomes'])
print(x['idades'])
print(x['alturas'])

y = {'nomes': [], 'idades': []}
print(y['nomes'])
y['nomes'].append('Eudes Leonnan')
y['nomes'].append('Renata Gomes')
print(y)
y['idades'].append(34)
y['idades'].append(30)
print(y)
print(y['nomes'])
print(y['idades'][1])

pessoas = [{'nomes': 'Eudes Leonnan', 'idades': 34, 'altura': 1.70 }, 
           {'nomes': 'Renata Gomes', 'idades': 30, 'altura': 1.70 },
           {'nomes': 'Roberto Fernandes', 'idades': 64, 'altura': 1.70}]
print(pessoas)
for pessoa in pessoas:
    print(pessoa)


for pessoa in pessoas:
    print(pessoa['nomes'])