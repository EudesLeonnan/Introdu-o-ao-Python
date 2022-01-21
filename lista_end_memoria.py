a  = 2
b = a
print(a)
print(b)
print(id(a))
print(id(b))

b = 3
print(a)
print(b)
print(id(a))
print(id(b))

x = [1, 2, 3]
y = x
y[0] = 0
print(x)
print(y) 
print(id(x))
print(id(y))

z = x.copy()
print(z)
x[2] = 'Eudes'
print(z)
print(x)
print(y)