# lists

a = [1, 2, 3, 4]
print(a)

b = ["jatin", 1, 1.5, print]
print(b)

a = [1, 2, 3, 4]
a[0] = 100
print(a)

print(len([1, 2, 3, 4]))
print("jatin" + "katyal")
print([1, 2, 3] + [4, 5 ,6])
print([1] * 4)

a = [1, 2, 3, 4, 5]
for x in a:
    print(x)

print("z" in "jatin")
print(1 in [1, 2, 3, 4])


a = [1, 2, 3, 4, 5]
print(a[-1])

a = [1, 2, 3]
a.insert(1, 100)
print(a)

a = [1, 2, 3, 4]
a.append(5)
print(a)

a = [1, 2, 3, 4, 5]
a.pop()
print(a)

a = [1, 2, 3, 4]
print(a)

a = ["jatin", "amarnath", "jatin", "shubham"]
a.remove("jatin")
print(a)
a.remove("jatin")
print(a)

a = [4, 1, 3, 2, 6, 4]
a.sort()
print(a)

b = [4, 1, 3, 2, 6, 4]
sorted(b)
print(b)

a = [1, 2, 3, 4, 5]
a.reverse()
print(a)

b = [1, 2, 3, 4, 5]
reversed(b)

for x in reversed(b):
    print(x)

a = [1, 2, 3, 4]
b = [1, 4, 9, 16]
for x in map(lambda x: x**2, a):
    print(x)

for i, x in enumerate(a):
    pass

def sqr(x):
    return x**2

a = map(int, input().split())
print(a)

print(a[0])












