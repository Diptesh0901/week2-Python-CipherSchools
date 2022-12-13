# COMPREHENSION -->

print(list(map(lambda x: x**2, range(5))))

a = []
for i in range(5):
    a.append(i**2)

print(a)

print([i for i in range(5)])

a = []
for i in range(5):
    temp = []
    for j in range(5):
        temp.append(j)
    a.append(temp)

    print(a)

n = 5
print([ [ max(i+1, j+1, n-i, n-j) for j in range(n) ] for i in range(n) ])

a = []
for i in range(3):
    for j in range(2):
        a.append(j)

print(a)

print([ j for i in range(5) for j in range(2)])

a = { i for i in range(5) }
print(type(a))

a = ( i for i in range(5) )
print(type(a))

for x in a:
    print(x)