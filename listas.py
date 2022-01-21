nomes = ['Caio', 'Marcos', 'Joao', 'Pedro']

print(type(nomes))
print(nomes)
print(nomes[1])
print(len(nomes))

nomes.append('Roberto')
print(nomes)
nomes[0] = 'Eudes'
print(nomes)

nomes[3] = 'Eudes Leonnan'
print(nomes)


nomes.append(2.3)
print(nomes)
nomes.append(True)
print(nomes)
nomes.append(["lala"])
print(nomes)

nomes.insert(0, 'Eudes Leonnan')
print(nomes)

nomes.pop()
print(nomes)

nomes.pop(0)
print(nomes)
nomes.pop(5)
print(nomes)

nomes.remove(True)
print(nomes)
nomes.remove('Eudes Leonnan')
nomes.insert(3, 'Eudes')
print(nomes)
nomes.remove('Eudes')
print(nomes)

nomes.index('Eudes')
print(nomes.index('Eudes'))

nomes.pop(nomes.index('Eudes'))
print(nomes)

nomes.append('Ana')
nomes.append('Bia')
nomes.append('Carla')
print(nomes)

nomes.sort()
print(nomes)

numeros = [8, 3, 9, 9, 8, 1, 1, 1, 6, 9, 19.2, 1.5]
numeros.sort()
print(numeros)

numeros.sort(reverse=True)
print(numeros)

sorted(numeros)
print(numeros)
print(sorted(numeros))
print(numeros)

idades = [12, 14, 20, 15, 34, 1, 40, 59, 32]
print(idades)
for i in range(0, len(idades)):
    print(i)
    print(idades[i])
    print(f'Na posição {i} temos a idade {idades[i]}')

for i in idades:
    print(f'Temos a idade {i}')

x = list(enumerate(idades))
print(x)

for i in enumerate(idades):
    print(i)
    print(i[0])
    print(i[1])

for i, j in enumerate(idades):
    print(f'Na posição {i} temos a idade {j}')

idades_de_maior = []
for i in idades:
    if i >= 18:
        idades_de_maior.append(i)
print(idades_de_maior)