#Matriz
idades = [['Eudes', 'Renata', 'Roberto', 'Ieda', 'Nildo', 'Karol'], 
          [34,         30,        62,      63,      62,      27]]
print(idades[1][4])
print(idades[0])
print(idades[1])

#No python temos listas de listas
idades = [['Eudes', 'Renata', 'Roberto', 'Ieda', 'Nildo', 'Karol'], 
          [34,         30,        62,      63,      62,      27,     38,     42]]
print(idades[1][4])
print(idades[0])
print(idades[1])
print(idades[1][7])

for i in range(0, len(idades)):  
    print(i)
    print(idades[i])

for i in range(0, len(idades)):  
    for j in range(0, len(idades[i])):
        print(idades[i][j])