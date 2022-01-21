x = { 'nomes': 'Eudes Leonnan', 'idades': 34, 'alturas': 1.70 }

print(x)
print(x['nomes'])
print(x['idades'])
print(x['alturas'])

y = {'nomes': [], 'idades': []}
print(y['nomes'])
y['nomes'].append('Eudes Leonnan')
y['nomes'].append('Renata Gomes')
y['nomes'].append('Robeto Fernandes')
print(y)
y['idades'].append(34)
y['idades'].append(30)
y['idades'].append(64)
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

y['cep'] = [ '58416-085', '58416-085', '58064-620']
print(y)

y.update({'CPF': ['123123123123-99', '345345345345-99', '567567567567-99']})
print(y)