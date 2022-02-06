n1 = int(input('Digite um número'))
n2 = int(input('Digite um número'))

#print(n1 / n2)

try:
    print(n1 / n2)
except:
    print('Não consegui')
finally:
    print('Finalizado')

try:
    x = int(input('Digite um número: '))
    print(5/x)
except ValueError:
    print('Digite um número inteiro!')
except ZeroDivisionError:
    print('Não digite 0')

try:
    x = int(input('Digite um número: '))
    print(5/x)
except Exception as e:
    print(e)

#Costumasse armazenar a excessão ou erro dentro de um arquivo
