pessoas = {'nomes': 'Eudes Leonnan', 'idades': 34, 'altura': 1.70 } 
       
print(pessoas.values())
print(pessoas.keys())
print(pessoas.items())

for i in pessoas: #Ele me traz apenas as chaves
    print(i)

for i in pessoas.items(): #Ele me traz tuplas com a chave e o valor
    print(i)
    print(i[0]) #Ele me traz apenas a chave
    print(i[1]) #Ele me traz apenas o valor

for i, j in pessoas.items(): #Ele faz uma descompressão
    print(f'{i}: {j} ')