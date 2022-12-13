# Lambda Expressions

print("Hello World")

def func():
    return 1+4
a = func
print(a())

print(lambda a, b: a + b)
show = print
show("something")

names = ["jatin", "saransh", "shubham", "samarth"]

for i, name in enumerate(names):
    print(i, "_", name)

a = 5
b = 9

temp = a
a = b
b = temp

a = a+b
b = a-b
a = a-b

print(a, b)

# packing and unpacking values

a = 5
b = 9

a, b = b, a
print(a, b)

a = [1, 2]
b, c = a
print(b,c)

a = (1, 2)
print(type(a))

names = ["jatin", "saransh", "shubham", "samarth"]
scores = [50, 80, 90, 70]

for a in zip(names, scores):
    print(a)

