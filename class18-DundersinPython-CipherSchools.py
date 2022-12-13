# Dunders(magic methods)


class A:
    def __init__(self):
        print(self)
        print("initialized")

    def __del__(self):
        print("I am Dancing")

a = A()

class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hello, my name is', self.name)

p = Person('Nikhil')
p.say_hi()

del a

a = 1
print(type(a))
print(a + 5)
print(a.__add__(5))

print("jatin" * 2)
print("jatin".__mul__(2))

class A:
    a = 1
    b = 2

    def __add__(self, x):
        return self.a + self.b + x

