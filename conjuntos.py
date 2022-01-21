x = [1, 1, 1, 1, 2, 3, 4, 5, 5, 5.0]
print(x)

x = set(x)
print(x)

y = {1, 1, 1, 1, 2, 3, 4, 5, 5, 5.0}
z = {5, 6, 7, 8, 9}

a = x.union(z)
print(a)

b = x.intersection(z)
print(b)

c = x.difference(z)
print(c)

d = x.symmetric_difference(z)
print(d)