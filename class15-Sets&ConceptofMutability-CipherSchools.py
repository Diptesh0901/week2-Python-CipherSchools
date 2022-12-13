# SETS

a = {1, 2, 3, 4}
print(type(a))

a.add(7)
a.remove(3)
a.add(2)

for i in a:
    print(i)

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a - b)

print(a.union(b))
print(a.intersection(b))
print(a.add(1))
print(a.remove(4))
print(a)

a = [[''] * 3] * 3
a[1][1] = 'X'
print(a)

print(id(a[0][1]))
print(id(a[1][2]))
print(id(a[2][1]))

print(id(1))
a[0] = 100
a = 1
print(id(a))
a = 2
print(id(a))

class Students:
    name = "Tony"
    marks = 60

a = 258
b = 258
print(a == b)
print(a is b)

