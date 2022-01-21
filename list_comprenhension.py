x = [i for i in range(0, 10)]
print(x)

y = []
for i in range(0, 10):
    y.append(i)
print(y)

x = [10 for i in range(0, 10)]
print(x)

x = [i*2 for i in range(0, 10)]
print(x)

x = [input('Digite um nome') for i in range(0, 3)]
print(x)

z = [[] for i in range(0, 3)]
print(z)

k = [[j for j in range(4, 7)] for i in range(0, 3)]
print(k)

a = [[input() for j in range(4, 7)] for i in range(0, 3)]
print(a)

b = [i for i in range(0, 20) if i%2==0]
print(b)
c = []
for i in range(0, 20):
    if i%2==0:
        c.append(i)
print(c)